import unittest
from unittest.mock import patch
from io import StringIO
from app import main

class TestApp(unittest.TestCase):
    @patch('builtins.input', side_effect=['John Doe', 'Tech Weekly', 'Technology', 'Sample Article', 'Lorem ipsum...'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout, mock_input):
        main()
        
        output = mock_stdout.getvalue()
    
        self.assertIn("Magazines:", output)
        self.assertIn("Tech Weekly", output)
        self.assertIn("Authors:", output)
        self.assertIn("John Doe", output)
        self.assertIn("Articles:", output)
        self.assertIn("Sample Article", output)
        self.assertIn("Lorem ipsum...", output)

if __name__ == "__main__":
    unittest.main()
