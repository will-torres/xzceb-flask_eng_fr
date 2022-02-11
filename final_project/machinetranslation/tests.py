import unittest
from translator import englishToFrench, frenchToEnglish
class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour") 
        self.assertEqual(englishToFrench("Chocolate"), "Chocolat")
        self.assertEqual(englishToFrench("Wine"), "Vin")
        self.assertEqual(englishToFrench("Cheese"), "Fromage")

class TestfrenchToEnglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") 
        self.assertEqual(frenchToEnglish("Chocolat"), "Chocolate")
        self.assertEqual(frenchToEnglish("Vin"), "Wine")
        self.assertEqual(frenchToEnglish("Fromage"), "Cheese")
        
unittest.main()