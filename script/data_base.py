""" Main file data base cahndling """
import sqlite3
from collections import namedtuple

Entity = namedtuple("Entity", "name email_adres title borrowed_at returned_at")


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


def get_borwers_by_return_date(connection, date_returned_at):
    entities = []
    with BaseConnectManager(connection) as database:
        database.cursor.execute(
            '''SELECT 
            name, 
            email_adres, 
            title, 
            borrowed_at, 
            returned_at 
        FROM borowers
        WHERE returned_at < ?''', (date_returned_at,))
        for name, email_adres, title, borrowed_at, returned_at in database.cursor.fetchall():
            entities.append(Entity(name, email_adres, title,
                            borrowed_at, returned_at))

    return entities


if __name__ == "__main__":
    connection = sqlite3.connect("database.db")

    # from datetime import datetime
    # datetime.today().strftime('%Y-%m-%d')
    borowers = get_borwers_by_return_date(connection, "2024-05-25")
    print(borowers)
