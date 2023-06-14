import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    
    def test_english_to_french(self):
        self.assertEqual(english_to_french("hello"), "bonjour")
        self.assertNotEqual(english_to_french("hello"), "hello")  # ensures that the text is translated
        
    def test_french_to_english(self):
        self.assertEqual(french_to_english("bonjour"), "hello")
        self.assertNotEqual(french_to_english("bonjour"), "bonjour")  # ensures that the text is translated

if __name__ == "__main__":
    unittest.main()
