from database.connection import get_db_connection
from models.author import Author
from models.magazine import Magazine

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        if not isinstance(content, str) or len(content) == 0:
            raise ValueError("Content must be a non-empty string")
        if not isinstance(author_id, int):
            raise ValueError("author_id must be an integer")
        if not isinstance(magazine_id, int):
            raise ValueError("magazine_id must be an integer")

        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

        if id is None:
            self._create_in_db()

    def _create_in_db(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)
        ''', (self.title, self.content, self.author_id, self.magazine_id))
        self.id = cursor.lastrowid
        connection.commit()
        connection.close()

    def __repr__(self):
        return f'<Article {self.title}>'

    @property
    def author(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM authors WHERE id = ?', (self.author_id,))
        author_data = cursor.fetchone()
        connection.close()
        return Author(author_data['id'], author_data['name']) if author_data else None

    @property
    def magazine(self):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM magazines WHERE id = ?', (self.magazine_id,))
        magazine_data = cursor.fetchone()
        connection.close()
        return Magazine(magazine_data['id'], magazine_data['name'], magazine_data['category']) if magazine_data else None

    @staticmethod
    def get_articles_by_author(author_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM articles WHERE author_id = ?', (author_id,))
        articles_data = cursor.fetchall()
        connection.close()
        return [Article(data['id'], data['title'], data['content'], data['author_id'], data['magazine_id']) for data in articles_data]

    @staticmethod
    def get_articles_by_magazine(magazine_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM articles WHERE magazine_id = ?', (magazine_id,))
        articles_data = cursor.fetchall()
        connection.close()
        return [Article(data['id'], data['title'], data['content'], data['author_id'], data['magazine_id']) for data in articles_data]

