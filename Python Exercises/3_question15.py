import unittest
import string
# import re

# Remove special symbols/Punctuation from a given string

def remove_special_chars(input_string):
    result = input_string.translate(str.maketrans('', '', string.punctuation))
    # result = re.sub(r'[^\w\s]', '', input_string)
    return result

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str = "/*Jon is @developer & musician"
        self.result = "Jon is developer  musician"

    def test01(self):
        self.assertEqual(remove_special_chars(self.str), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.str
        del self.result

if __name__ == "__main__":
    unittest.main()
