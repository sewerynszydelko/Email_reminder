from data_base import get_title_authors, create_connection
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
