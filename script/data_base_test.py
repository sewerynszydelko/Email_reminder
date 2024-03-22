from data_base import get_title_authors, create_connection, get_all_books_from_db
import sqlite3


def test_get_title_authors():
    # Given
    conection = sqlite3.Connection(':memory:')
    cursor = conection.cursor()
    cursor.execute('''CREATE TABLE books
                    (id integer, title text, author text, created_at datae)''')
    sample_data = [
        (1, 'Pan Samochodzik', 'Zbigniew Niemacki', '2019-02-03 20:12:22'),
        (1, 'W pustyni i w puszczy', 'Henryk Sienkiewicz', '2018-06-23 12:20:50')
    ]
    cursor.executemany('INSERT INTO books VALUES(?, ?, ?, ?)', sample_data)

    # When
    data = get_title_authors(cursor)

    # Then
    print(data)


def test_get_all_books_from_db():
    # Given
    connection = sqlite3.Connection(":memory:")
    cursor = connection.cursor()
    cursor.execute(
        'CREATE TABLE books2 (id integer, email text, title text, author text, created_at datae)')
    sample_data = [
        (1, 'Pan Samochodzik', 'example22@gmail.com',
         'Zbigniew Niemacki', '2019-02-03 20:12:22'),
        (2, 'W pustyni i w puszczy', 'example!@wp.pl',
         'Henryk Sienkiewicz', '2018-06-23 12:20:50')
    ]
    cursor.executemany('INSERT INTO books2 VALUES(?, ?, ?, ?, ?)', sample_data)
    # When
    data = get_all_books_from_db("base.db")

    # Then
    print(data)
