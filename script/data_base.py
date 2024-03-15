import sqlite3


def create_connection():
    with sqlite3.connect('base.db') as connection:
        cursor = connection.cursor()
        # cursor.execute('SELECT * FROM books WHERE authors=?', ('Henryk Sienkiewicz',))

    return cursor


def get_authors(cursor):
    cursor.execute('SELECT * FROM books')
    data = []
    for book in cursor.fetchall():
        book_id, title, author, created_at = book
        data.append({
            'title': title,
            'author': author
        })

    return data

if __name__ == "__main__":
    cursor = create_connection()
    authors = get_authors(cursor)
    print(authors)