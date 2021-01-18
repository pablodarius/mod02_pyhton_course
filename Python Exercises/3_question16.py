import unittest
import re

# Removal all the characters other than integers from string

def remove_not_digits(input_string):
    result = re.findall('[0-9]+', input_string)
    return int("".join(result))
    

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str = "I am 25 years and 10 months old"
        self.result = 2510

    def test01(self):
        self.assertEqual(remove_not_digits(self.str), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.str
        del self.result

if __name__ == "__main__":
    unittest.main()
