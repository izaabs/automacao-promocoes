import time
from pathlib import Path
from playwright.sync_api import sync_playwright
from main import processar_mensagem

NOME_GRUPO = 'Promos de Paty #57'
PASTA_PROJETO = Path(__file__).resolve().parent
PASTA_PERFIL = PASTA_PROJETO / 'perfil_whatsapp'


with sync_playwright() as p:
    navegador = p.chromium.launch_persistent_context(
        user_data_dir = str(PASTA_PERFIL),
        headless = False
    )

    pagina = navegador.pages[0]
    pagina.goto('https://web.whatsapp.com')
    print('Whatsapp Web aberto! Faça a leitura do QR Code se necessário')

    pagina.wait_for_timeout(20000) # Espera 20 segundos para o usuário escanear o QR Code

    # Procura a caixa de pesquisa em português ou inglês
    campo_pesquisa = pagina.locator(
        'input[aria-label="Search or start a new chat"], '
        'input[aria-label="Pesquisar ou iniciar nova conversa"]'
    )

    campo_pesquisa.wait_for(state = 'visible', timeout = 40000) # Espera até 40 segundos
    campo_pesquisa.click()
    campo_pesquisa.fill(NOME_GRUPO)
    
    print(f'Pesquisando pelo grupo: {NOME_GRUPO}')
    pagina.wait_for_timeout(3000) # Espera 3 segundos para o grupo aparecer na lista

    resultados = pagina.get_by_role(
        'gridcell',
        name = NOME_GRUPO,
        exact = False
    )

    print(f'Resultados encontrados: {resultados.count()}')

    resultados.first.click()
    print(f'Grupo {NOME_GRUPO} aberto com sucesso!')

    pagina.wait_for_timeout(3000)

    print('\n--- MENSAGENS JÁ CARREGADAS ---')
    mensagens = pagina.locator('[data-pre-plain-text]') # Seleciona as msgs do grupo
    msgs_processadas = set()  # Lista de memória das msgs
    quantidade_msg = mensagens.count()

    print(f'Quantidade de mensagens encontradas: {quantidade_msg}')

    for i in range(quantidade_msg):
        texto = mensagens.nth(i).inner_text() # Pega o texto da msg
        msgs_processadas.add(texto)

    print('\n👀 Monitorando novas mensagens...')

    try:
        while True:
            quantidade_msg = mensagens.count()

            for i in range(quantidade_msg):
                texto = mensagens.nth(i).inner_text()

                if texto not in msgs_processadas:
                    print('\n🆕 Nova mensagem encontrada!')
                    print(texto)
                    processar_mensagem(texto)
                    msgs_processadas.add(texto)

            time.sleep(30)  # Espera 30 segundos antes de verificar novamente

    except KeyboardInterrupt:
        print('\nMonitoramento encerrado pelo usuário.')