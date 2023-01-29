import unittest

from translator import MachineTranslation

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(MachineTranslation.english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(MachineTranslation.english_to_french('Bonjour'), 'Hello')
    
    def test_french_to_english(self):
        self.assertEqual(MachineTranslation.french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(MachineTranslation.french_to_english('Hello'), 'Bonjour')

if __name__ == '__main__':
    unittest.main()