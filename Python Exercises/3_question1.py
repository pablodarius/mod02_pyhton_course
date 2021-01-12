import unittest

# Given a string of odd length greater 7, return a string made of the middle three chars of a given String

def middle_string(sentence):
    middle = len(sentence) // 2
    return sentence[middle - 1 : middle + 2]

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str1 = "JhonDipPeta"
        self.str2 = "JaSonAy"
        self.result1 = "Dip"
        self.result2 = "Son"

    def test01(self):
        self.assertEqual(middle_string(self.str1), self.result1)

    def test02(self):
        self.assertEqual(middle_string(self.str2), self.result2)

    def tearDown(self):
        print("Deleting context...")
        del self.str1
        del self.str2
        del self.result1
        del self.result2

if __name__ == "__main__":
    unittest.main()
