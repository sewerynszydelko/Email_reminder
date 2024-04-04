from data_base import BaseConnectManager
from collections import namedtuple

Entity = namedtuple("Entity", "name email_adres title borrowed_at returned_at")


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


# from datetime import datetime
# datetime.today().strftime('%Y-%m-%d')
borowers = get_borwers_by_return_date(connection, "2024-05-25")
print(borowers)
