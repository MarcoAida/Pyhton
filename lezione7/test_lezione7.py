#python -m unittest discover

import unittest

from lezione7 import somma

class TestSomma(unittest.TestCase):
    def test_somma(self):

        self.assertEqual(somma(1,1), 2)
        self.assertEqual(somma(1.5,2.5), 4)
        
class TestSomma2(unittest.TestCase):
    def test_somma(self):
    
        self.assertEqual(somma(1,2), 4)

class TestSomma3(unittest.TestCase):
    def test_somma(self):
       
        try:
            self.assertEqual(somma(1,2), 4)

        except Exception:
            print('Error')    