""" Email sender file """
from collections import namedtuple
import smtplib
import ssl

# Stable data not cahngble as class but not modyfing
User = namedtuple("User", "name surname")
example_user = User("Bob", "Crouch")


def send_mail():
    smtp_server = "smtp.gmail.com"
    port = 465
    sender_email = "Your email @gamil.com"
    password = 'Your password'

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port=port, context=context) as server:
        server.login(sender_email, password=password)
        server.sendmail(sender_email, sender_email, "user is cool")
