""" Email sender file """
import smtplib
import ssl

class EmailSender:
    def __init__(self, port, smtp_server, credentials, ssl_enable=False):
        self.port = port
        self.smtp_server = smtp_server
        self.ssl_enable = ssl_enable
        self.connection = None
        self.credentials = credentials

    def __enter__(self):
        if not self.ssl_enable:
            self.connection = smtplib.SMTP(smtp_server, port)
        else:
            context = ssl.create_default_context()
            self.connection = smtplib.SMTP_SSL(
                self.smtp_server, self.port, context)

        self.connection.login(self.credentials.username,
                              self.credentials.password)

        return self

    def sendmail(self, sender, receiver, message):
        self.connection.sendmail(sender, receiver, message.as_string())

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
