import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText

load_dotenv()

def enviar_email(promocao):
    remetente = 'izabelliribeiros@gmail.com'
    senha_app = os.getenv('GMAIL_SENHA')
    destinatario = 'izabelliribeiros@gmail.com'

    assunto = f'🔥 Promoção encontrada: {promocao["produto"]}'
    corpo_email = f'''
            Promoção encontrada!
            Produto: {promocao["produto"]}
            Preço original: {promocao["preco_original"]}
            Preço promocional: {promocao["preco_promocional"]}
            Desconto: {promocao["desconto"]}%
            Cupom: {promocao["cupom"]}
        '''

    mensagem_email = MIMEText(corpo_email)
    mensagem_email['Subject'] = assunto
    mensagem_email['From'] = remetente
    mensagem_email['To'] = destinatario

    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)

        servidor.starttls()
        servidor.login(remetente, senha_app)
        servidor.send_message(mensagem_email)
        servidor.quit()
        print('E-mail enviado com sucesso!')

    except Exception as erro:
        print(f'Erro ao enviar e-mail: {erro}')