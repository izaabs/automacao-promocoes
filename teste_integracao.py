from main import processar_mensagem

mensagem_teste = """
Epidrat Calm B5 50ml

de R$ 89,90

por R$ 58,90

Use o cupom: CALM10
"""


print('--- TESTE DE INTEGRAÇÃO ---')

processar_mensagem(mensagem_teste)