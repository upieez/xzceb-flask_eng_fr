import unittest

from translator import machinetranslation

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(machinetranslation.englishToFrench('Hello'), 'Bonjour')
        self.assertNotEqual(machinetranslation.englishToFrench('Bonjour'), 'Hello')
    
    def test_french_to_english(self):
        self.assertEqual(machinetranslation.frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(machinetranslation.frenchToEnglish('Hello'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()