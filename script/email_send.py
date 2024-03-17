""" Email sender file """
import smtplib
import ssl


def send_mail():
    smtp_server = "smtp.gmail.com"
    port = 465
    sender_email = "Your email @gamil.com"
    password = 'Your password'

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port=port, context=context) as server:
        server.login(sender_email,password=password)
        server.sendmail(sender_email,sender_email,"user is cool")