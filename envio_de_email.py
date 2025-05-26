import os
import pathlib
from dotenv import load_dotenv 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

print('Enviando email...')

CAMINHA_HTML = pathlib.Path(__file__).parent / 'Emails_html' /'emailCurriculo.html'

# dados do remetente e destinatario 
remetente = os.getenv('FROM_EMAIL','')
destinatario = remetente
assunto = 'Assunto do email teste'

#Configurando SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL','')
smtp_password = os.getenv('EMAIL_PASSWORD','')

# Mensagem de Texto
with open(CAMINHA_HTML,'r') as file:
    texto_arquivo = file.read()
    
# Transformando a mensagem em MINEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = assunto

body_email = MIMEText(texto_arquivo, 'html', 'utf-8')
mime_multipart.attach(body_email)


with smtplib.SMTP(smtp_server,smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username,smtp_password)
    server.send_message(mime_multipart)
    print('Email enviado com sucesso!')