""" Main file """
import email
import sqlite3
from collections import namedtuple
from string import Template
from os import getenv
from dotenv import load_dotenv
from borrowers import get_borwers_by_return_date
from email_send import EmailSender

load_dotenv()
connection_sq = sqlite3.connect(getenv("DB_NAME"))

ssl_enable = getenv("SSL_ENABLE")
port = getenv("PORT")
smtp_server = getenv("SMTP_SERVER")
username = getenv("USERNAME_EMAIL")
password = getenv("PASSWORD")

sender = getenv("SENDER")
subject = getenv("SUBJECT")


Credentials = namedtuple("Credentials", "username password")
credentials = Credentials(username, password)


def send_reminder_to_borrower(borower):

    template = Template('''Hey $name!
Remember, you have my book: $title !
Pleas give it back to me as quick as posible
Return date: $returned_at

I'm Waiting
    ''')
    text_msg = template.substitute({
        'name': borower.name,
        'title': borower.title,
        'returned_at': borower.returned_at
    })

    message = email.message_from_string(text_msg)

    message.set_charset("utf-8")
    message["From"] = sender
    message["To"] = borower.email_adres
    message["Subject"] = subject

    connection.sendmail(sender, borower.email_adres, message)
    print(f"Sending to: {borower.email_adres}")


if __name__ == "__main__":

    borrowers = get_borwers_by_return_date(connection_sq, "2024-05-24")

    with EmailSender(port, smtp_server, credentials) as connection:
        for borower in borrowers:
            send_reminder_to_borrower(borower)


# from datetime import datetime
# datetime.today().strftime('%Y-%m-%d')
