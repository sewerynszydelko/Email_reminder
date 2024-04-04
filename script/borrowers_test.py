""" File test for borrowers """
import pytest
import sqlite3
from borrowers import get_borwers_by_return_date


@pytest.fixture
def create_connection():
    connection = sqlite3.Connection(":memory:")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE borowers(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   email_adres TEXT,
                   title TEXT,
                   borrowed_at DATE,
                   returned_at DATE)''')
    sample_data = [
        (1, "Adam", "adam222@gamil.com", "Atals", "2022-02-15", "2023-06-25"),
        (2, "Bob", "bob@example.com", "Bible", "2023-10-02", "2024-01-18"),
        (3, "Henry", "henryko@gamil.com", "Quo Vadis", "2023-09-03", "2024-04-06")
    ]

    cursor.executemany("INSERT INTO borowers VALUES (?, ?, ?, ?, ?, ?)",sample_data)

    return connection


def test_borrows(create_connection):
    # Given
    borowers = get_borwers_by_return_date(create_connection,"2024-04-06")
    assert borowers[0].name == "Adam"
    assert borowers[1].name == "Bob"
    assert len(borowers) == 2