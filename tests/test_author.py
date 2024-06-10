import unittest
from models.author import Author

class TestAuthor(unittest.TestCase):
    def test_author_creation(self):
        author = Author(id=1, name="John Doe")
        self.assertEqual(author.name, "John Doe")



if __name__ == "__main__":
    unittest.main()
