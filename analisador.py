import re

# Função que procura o produto mais parecido
def verificar_promocao(mensagem, wishlist):
    mensagem = mensagem.lower()

    melhor_produto = None
    maior_pontuacao = 0

    for produto in wishlist['produtos']:
        pontuacao = 0

        for palavra in produto['palavras_chave']:
            palavra = palavra.lower()

            # Ignora medidas genéricas, como 50ml e 40g
            if re.fullmatch(r'\d+\s*(ml|g)', palavra):
                continue

            padrao = r'(?<!\w)' + re.escape(palavra) + r'(?!\w)'

            if re.search(padrao, mensagem):
                pontuacao += 1
                print(
                    f'🔎 Correspondência encontrada: '
                    f'"{palavra}" -> {produto["nome"]}'
                )

        if pontuacao >= 2 and pontuacao > maior_pontuacao:
            melhor_produto = produto['nome']
            maior_pontuacao = pontuacao

    return melhor_produto # Retorna o produto que teve mais correspondências


# Função para extrair preços da mensagem
def extrair_precos(mensagem):
    precos = re.findall(r'R\$\s*[\d.,]+', mensagem)

    preco_original = None
    preco_promocional = None

    if len(precos) >= 2:
        preco_original = precos[0]
        preco_promocional = precos[1]

    return preco_original, preco_promocional


# Função para extrair cupom
def extrair_cupom(mensagem):
    resultado = re.search(
        r'cupom:\s*([A-Z0-9]+)', 
        mensagem, 
        re.IGNORECASE
    )

    if resultado:
        return resultado.group(1)

    return None


# Função para calcular o percentual de desconto
def calcular_desconto(preco_original, preco_promocional):
    preco_original = float(
        preco_original.replace('R$', '').replace('.', '').replace(',', '.')
    )

    preco_promocional = float(
        preco_promocional.replace('R$', '').replace('.', '').replace(',', '.')
    )

    desconto = ((preco_original - preco_promocional) / preco_original) * 100
    return round(desconto, 2)


# 6. Função principal que integra todas as funcionalidades
def analisar_promocao(mensagem, wishlist):
    produto = verificar_promocao(mensagem, wishlist)

    if produto is None:
        return None
    
    preco_original, preco_promocional = extrair_precos(mensagem)
    cupom = extrair_cupom(mensagem)
    desconto = None

    if preco_original and preco_promocional:
        desconto = calcular_desconto(preco_original, preco_promocional)

    promocao = {
        'produto': produto,
        'preco_original': preco_original,
        'preco_promocional': preco_promocional,
        'desconto': desconto,
        'cupom': cupom
    }

    return promocao