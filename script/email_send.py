""" Email sender file """
from collections import namedtuple
import smtplib
import ssl

# Stable data not cahngble as class but not modyfing
User = namedtuple("User", "name surname")
example_user = User("Bob", "Crouch")


def send_mail(message: str):
    """ Sending email
    Args:
        message (str): mesage in email to send
    """
    smtp_server = "smtp.wp.pl"
    port = 465
    sender_email = "@gmail"
    password = "#"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port=port, context=context) as server:
        server.login(sender_email, password=password)
        server.sendmail(sender_email, sender_email, message)
        print("meesage sended")


def send_email2():

    ssl_enable = False
    port = 587
    smtp_server = "sandbox.smtp.mailtrap.io"
    username = "a##"
    password = "4##"

    subject = "Give back book!"
    sender = "Serwe <@gmail.com>"
    receiver = "Test WP <l@wp.pl>"

    message = f"""\
    Subject: {subject}
    To: {receiver}
    From: {sender}

    This is a test e-mail message."""

    if not ssl_enable:
        connection = smtplib.SMTP(smtp_server, port)
    else:
        context = ssl.create_default_context()
        connection = smtplib.SMTP_SSL(smtp_server, port, context)

    connection.login(username, password)
    connection.sendmail(sender, receiver, message)
    print("closing")
    connection.close()

    """
    with smtplib.SMTP(smtp_server, 2525) as server:
        server.login(username, password)
        server.sendmail(sender, receiver, message)
    """


if __name__ == "__main__":
    # send_email2()

    sender = "Private Person <@gmail.com>"
    receiver = "A Test User <@wp.pl>"

    message = f"""\
    Subject: Hi Mailtrap
    To: {receiver}
    From: {sender}

    This is a test e-mail message."""

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        server.login("", "")
        server.sendmail(sender, receiver, message)
