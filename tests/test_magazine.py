import unittest
from models.magazine import Magazine

class TestMagazine(unittest.TestCase):
    def test_magazine_creation(self):
        magazine = Magazine(id=1, name="Tech Weekly", category="Technology")
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")


if __name__ == "__main__":
    unittest.main()

