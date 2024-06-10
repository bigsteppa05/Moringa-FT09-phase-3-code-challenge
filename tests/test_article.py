import unittest
from models.article import Article

class TestArticle(unittest.TestCase):
    def test_article_creation(self):
        article = Article(id=1, title="Sample Article", content="Lorem ipsum...", author_id=1, magazine_id=1)
        self.assertEqual(article.title, "Sample Article")
        self.assertEqual(article.content, "Lorem ipsum...")
        self.assertEqual(article.author_id, 1)
        self.assertEqual(article.magazine_id, 1)



if __name__ == "__main__":
    unittest.main()
