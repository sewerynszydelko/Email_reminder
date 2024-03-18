import sqlite3


def create_connection():
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()
        # cursor.execute('SELECT * FROM books WHERE authors=?', ('Henryk Sienkiewicz',))

    return cursor


def get_title_authors(cursor):
    cursor.execute('SELECT * FROM books2')
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

# TODO - Get title_avible
# TODO - Get make column for avibility of book
# TODO - Insert new data to specific row
# TODO - Make user calss that can add his email and book


if __name__ == "__main__":
    cursor = create_connection()
    authors = get_title_authors(cursor)

    print("----"*10, "\n")

    emails_browed = get_emails_and_id(cursor)
