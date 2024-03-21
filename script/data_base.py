""" Main file data base cahndling """
import sqlite3


class BaseConnectManager:
    """ Contex menager for data base"""

    def __init__(self, data_base):
        self.data_base = data_base
        self.cursor = None
        self.connection = None
        pass

    def __enter__(self):
        print("conecting")
        with sqlite3.connect(self.data_base) as connection:
            cursor = connection.cursor()
        self.connection = connection
        self.cursor = cursor
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        print("closing")


def get_all_books_from_db(base_name: str) -> list:
    with BaseConnectManager(base_name) as cursor:
        cursor.exectue("SELECT * FROM books2")
        data = []

        for book in cursor.fetchall():
            book_id, email_adres, title, author, created_at = book
            data.append({
                "id": book_id,
                "email": email_adres,
                "title": title,
                "author": author,
                "created_at": created_at
            })


def create_connection():
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()

    return cursor


def get_title_authors(cursor):
    cursor.execute('SELECT * FROM books')
    data = []
    for book in cursor.fetchall():
        book_id, title, author, created_at = book
        data.append({
            'title': title,
            'author': author
        })

    return data


def get_emails_and_id(cursor):
    cursor.execute("SELECT * FROM books2")
    data = []

    for book in cursor.fetchall():
        book_id, email_adres, title, author, created_at = book
        data.append({
            "id": book_id,
            "email": email_adres,
        })

    return data


def add_new_book(email_adres: str, title: str, author: str, creted_at: str, base_name: str) -> None:
    with BaseConnectManager(base_name) as cursor:
        cursor.execute("INSERT INTO books2(email_adres ,title, author, created_at) VALUES(?, ?, ?, ?)",
                       (email_adres, title, author, creted_at))
        cursor.connection.commit()

if __name__ == "__main__":
    cursor = create_connection()
    authors = get_title_authors(cursor)

    print("----"*10, "\n")

    emails_browed = get_emails_and_id(cursor)

    """add_new_book("sienkiewicz@onet.pl", "Example1",
                 "Ali Ahmed", "2024-02-15 10:45:22","base.db")"""
