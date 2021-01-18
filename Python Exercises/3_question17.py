import unittest

# Find words with both alphabets and numbers

def find_word_with_digits(input_string):
    input_string = input_string.split()
    result = []
    for item in input_string:
        if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
            result.append(item)
    return result

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str = "Emma25 is Data scientist50 and AI Expert"
        self.result = ["Emma25", "scientist50"]

    def test01(self):
        self.assertEqual(find_word_with_digits(self.str), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.str
        del self.result

if __name__ == "__main__":
    unittest.main()
