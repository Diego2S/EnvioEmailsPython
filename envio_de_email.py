import os
import pathlib
from dotenv import load_dotenv 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_email(html,destinatario,assunto):

    load_dotenv()

    print('Enviando email...')

    CAMINHA_HTML = pathlib.Path(__file__).parent / 'Emails_html' /f'{html}'

    # dados do remetente e destinatario 
    remetente = os.getenv('FROM_EMAIL','')
    

    #Configurando SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = os.getenv('FROM_EMAIL','')
    smtp_password = os.getenv('EMAIL_PASSWORD','')

    try:
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
    
    except FileNotFoundError:
        print(f'❌ Arquivo HTML "{html}" não encontrado.')
        return
    except Exception as e:
        print(f'❌ Erro ao preparar o e-mail: {e}')
        return

    try:

        with smtplib.SMTP(smtp_server,smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.login(smtp_username,smtp_password)
            server.send_message(mime_multipart)
            print(f'✅ Email para ({destinatario})enviado com sucesso!')
    except smtplib.SMTPAuthenticationError:
        print('❌ Falha de autenticação. Verifique o e-mail e a senha.')
    except Exception as e:
        print(f'❌ Erro ao enviar o e-mail: {e}')



if __name__ == '__main__':

    for destinatario in ['',
              ""]:
        send_email('emailpersonalizado.html', # modelo HTML
            destinatario, # Destinatario
            'Curriculo - Diego Santos'# Assunto 
            )