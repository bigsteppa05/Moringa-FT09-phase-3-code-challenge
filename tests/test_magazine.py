import unittest
from unittest.mock import patch
from app import main

class TestApp(unittest.TestCase):
    @patch('builtins.input', side_effect=['John Doe', 'Tech Weekly', 'Technology', 'Sample Article', 'Lorem ipsum...'])
    def test_main(self, mock_input):
        # Simply call the main function and ensure it runs without raising exceptions
        main()

if __name__ == "__main__":
    unittest.main()


