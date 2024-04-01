""" Test data base file """
from data_base import get_title_authors, create_connection, get_all_books_from_db
import sqlite3


def test_get_title_authors():
    """ test get title from data base func , from test data memory"""
    # Given
    conection = sqlite3.Connection(':memory:')
    cursor = conection.cursor()
    cursor.execute('''CREATE TABLE books2
                    (id integer, email TEXT,title TEXT, author TEXT, created_at date)''')
    sample_data = [
        (1, 'jerzy@gmail.com', 'Pan Samochodzik',
         'Zbigniew Niemacki', '2019-02-03 20:12:22'),
        (1, 'arek@wp.pl', 'W pustyni i w puszczy',
         'Henryk Sienkiewicz', '2018-06-23 12:20:50')
    ]
    cursor.executemany('INSERT INTO books2 VALUES(?, ?, ?, ?, ?)', sample_data)

    # When
    data = get_title_authors(cursor)

    # Then
    print(data)


def test_get_all_books_from_db():
    """ Test func give all books from data base """
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
    data = get_all_books_from_db()

    # Then
    print(data)
