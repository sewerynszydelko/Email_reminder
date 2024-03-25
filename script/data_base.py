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
    """ Get all books from data base
    Args:
        base_name (str): data base name
    Returns:
        list: returns all books info in dictonary
    """
    with BaseConnectManager(base_name) as cursor:
        cursor.execute("SELECT * FROM books2")
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
    return data


def create_connection():
    """ Create conection to data base
    Returns:
        obj : cursor to data base
    """
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()

    return cursor


def get_title_authors(cursor):
    """ Get all titles and authors of books
    Args:
        cursor (obj): curosr to data base
    Returns:
        list : Return list with title and authors in dictionary
    """
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
    """ Get all emains and id
    Args:
        cursor (obj): curosr to data base
    Returns:
        list: list with id, emails in dictionary
    """
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
    """ Add new books with other info to data base
    Args:
        email_adres (str): email adres person
        title (str): title of book
        author (str): author of book
        creted_at (str): time when added to data base
        base_name (str): name to what data base insert
    """
    with BaseConnectManager(base_name) as cursor:
        cursor.execute("INSERT INTO books2(email_adres ,title, author, created_at) VALUES(?, ?, ?, ?)",
                       (email_adres, title, author, creted_at))
        cursor.connection.commit()


def update_column_row(row_name:str, value_row, id_num:int):
    """ Updatate column in specifuc row
    Args:
        row_name (str): name of row
        value_row (_type_): new value to row int or str
        id_num (int): id of row
    """
    try:
        with BaseConnectManager("base.db") as cursor:
            cursor.execute(f"UPDATE books2 SET {row_name}= '{value_row}' WHERE id={id_num}")
            cursor.connection.commit()
    except sqlite3.OperationalError as error:
        print(f"You put in wrong place {error}")


if __name__ == "__main__":
    cursor = create_connection()
    authors = get_title_authors(cursor)

    print("----"*10, "\n")

    emails_browed = get_emails_and_id(cursor)

