import unittest

# Count all lower case, upper case, digits, and special symbols from a given string

def count_chars(s1):
    chars = 0
    digits = 0
    symbol = 0

    for s in s1:
        if s.islower() or s.isupper():
            chars += 1
        elif s.isdigit():
            digits += 1
        else:
            symbol += 1

    return [chars, digits, symbol]

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str1 = "P@#yn26at^&i5ve"
        self.result = [8, 3, 4]

    def test01(self):
        self.assertEqual(count_chars(self.str1), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.str1
        del self.result

if __name__ == "__main__":
    unittest.main()
