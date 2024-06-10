from database.connection import get_db_connection

class Author:
    def __init__(self, id, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")

        self._id = id
        self._name = name
        if id is None:
            self._create_in_db()

    def _create_in_db(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (self._name,))
        self._id = cursor.lastrowid
        connection.commit()
        connection.close()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def articles(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''
            SELECT a.id, a.title FROM articles a
            JOIN authors au ON a.author_id = au.id
            WHERE au.id = ?
        ''', (self._id,))
        articles = cursor.fetchall()
        connection.close()
        return articles

    def magazines(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''
            SELECT DISTINCT m.id, m.name FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        ''', (self._id,))
        magazines = cursor.fetchall()
        connection.close()
        return magazines


