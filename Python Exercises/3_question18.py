import unittest
from string import punctuation

# From given string replace each punctuation with #

def replace_punctuation(input_string):
    for char in punctuation:
        input_string = input_string.replace(char, "#")
    return input_string

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str = "/*Jon is @developer & musician!!"
        self.result = "##Jon is #developer # musician##"

    def test01(self):
        self.assertEqual(replace_punctuation(self.str), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.str
        del self.result

if __name__ == "__main__":
    unittest.main()
