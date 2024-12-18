import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def enviar_email(caminho_relatorio, destinatario="destinatario@example.com"):
    remetente = "essim25silva@gmail.com"
    senha = "foig vjwu qrjr xwaa"
    destinatario = "edson25silva@outlook.pt"

    # Configurar a mensagem
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = "Relatório de Análise de Dados"

    corpo = """
    Olá,

    Segue em anexo o relatório de análise de dados gerado automaticamente.

    Atenciosamente,
    Equipe de Automação
    """
    msg.attach(MIMEText(corpo, 'plain'))

    # Anexar o relatório
    with open(caminho_relatorio, "rb") as anexo:
        parte = MIMEBase('application', 'octet-stream')
        parte.set_payload(anexo.read())
        encoders.encode_base64(parte)
        parte.add_header('Content-Disposition', f'attachment; filename={os.path.basename(caminho_relatorio)}')
        msg.attach(parte)

    # Enviar o e-mail
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remetente, senha)
        servidor.send_message(msg)
        servidor.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
