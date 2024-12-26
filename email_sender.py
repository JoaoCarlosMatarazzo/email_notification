import smtplib
from email.mime.text import MIMEText
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASSWORD

def send_email(to_email, subject, message):
    try:
        # Configurando o servidor SMTP
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)

        # Criando o e-mail
        msg = MIMEText(message, 'plain')
        msg['Subject'] = subject
        msg['From'] = EMAIL_USER
        msg['To'] = to_email

        # Enviando o e-mail
        server.sendmail(EMAIL_USER, to_email, msg.as_string())
        server.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
