import unittest

from driven import CSVFile

class TestCSVFile(unittest.TestCase):
    def test_init(self):
        csv_file = CSVFile('shampoo_sales_.csv') 
        
        self.assertEqual(testdriven.name, 'shampo_sales_.csv')