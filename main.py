from email_sender import send_email
from config import DEFAULT_MESSAGE

def main():
    print("Bem-vindo ao sistema de notificações por e-mail!")

    # Coleta de informações do usuário
    data = input("Digite a data (DD/MM/AAAA): ")
    hora = input("Digite a hora (HH:MM): ")
    local = input("Digite o local: ")
    email = input("Digite o seu e-mail: ")
    message = DEFAULT_MESSAGE.format(data=data, hora=hora, local=local)
    subject = "Sua Notificação"
    send_email(email, subject, message)
if __name__ == "__main__":
    main()
