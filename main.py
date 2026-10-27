import json
from pathlib import Path
from analisador import analisar_promocao
from notificacao import enviar_email


# Define o caminho da pasta do projeto
PASTA_PROJETO = Path(__file__).resolve().parent


# Carrega a lista de desejos
with open(PASTA_PROJETO / 'wishlist.json', 'r', encoding='utf-8') as arquivo:
    wishlist = json.load(arquivo)


# Função para verificar se a promoção já existe no histórico
def promocao_existente(promocao, historico):
    for promocao_salva in historico['promocoes']:
        if (
            promocao_salva['produto'] == promocao['produto']
            and promocao_salva['preco_promocional'] == promocao['preco_promocional']
            and promocao_salva['cupom'] == promocao['cupom']
        ):

            return True
    return False


# Função para salvar a promoção no histórico
def salvar_promocao(promocao):
    caminho_historico = PASTA_PROJETO/'historico.json'

    try:
        with open(caminho_historico, 'r', encoding='utf-8') as arquivo:
            historico = json.load(arquivo)

    except FileNotFoundError:
        print('Erro: o arquivo historico.json não foi encontrado.')
        return False

    except json.JSONDecodeError:
        print('Erro: o arquivo historico.json está vazio ou contém JSON inválido.')
        return False

    if promocao_existente(promocao, historico):
        print('Promoção já existe no histórico.')
        return False

    historico['promocoes'].append(promocao)

    with open(caminho_historico, 'w', encoding='utf-8') as arquivo:
        json.dump(
            historico,
            arquivo,
            ensure_ascii=False,
            indent=4
        )
    print('Promoção salva no histórico com sucesso!')
    return True


# Processa uma mensagem recebida do WhatsApp
def processar_mensagem(mensagem):
    promocao = analisar_promocao(mensagem, wishlist)

    if promocao is None:
        print('Nenhum produto da wishlist encontrado')
        return

    print('\n🚨 PROMOÇÃO DA WISHLIST ENCONTRADA!')
    print(f'Produto: {promocao["produto"]}')
    print(f'Preço: {promocao["preco_promocional"]}')
    print(f'Desconto: {promocao["desconto"]}%')
    print(f'Cupom: {promocao["cupom"]}')

    nova_promocao = salvar_promocao(promocao)

    if nova_promocao:
        enviar_email(promocao)

# zarf wnlr oemk wjlt