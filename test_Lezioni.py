import unittest

class TestGetData(unittest.TestCase):
    def TestGetData(self):
        mio_file = CSVFile(name='vendite.csv')
        self.assertEqual(mio_file.name, 'vendite.csv')
        
        
    