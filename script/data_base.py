""" Main file data base cahndling """


class BaseConnectManager:
    """ Contex menager for data base"""

    def __init__(self, connection):
        self.connection = connection
        self.cursor = None

    def __enter__(self):
        print("conecting")
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()

        self.connection.close()
        print("Closing Connection")
