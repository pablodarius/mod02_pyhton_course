import unittest

class PruebasMetodosCadenas(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('hola'.upper(), 'HOLA')

    def test_isupper(self):
        self.assertTrue('HOLA'.isupper())
        self.assertFalse('Hola'.isupper())

    def test_split(self):
        s = 'Hola Mundo'
        self.assertEqual(s.split(' '), ['Hola', 'Mundo'])

if __name__ == "__main__":
    unittest.main()