import unittest

# Given an input string, count occurrences of all characters within a string

def reverse_string(s):
    # return ''.join(reversed(s))
    return s[::-1]

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str = "PYnative"
        self.result = "evitanYP"

    def test01(self):
        self.assertEqual(reverse_string(self.str), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.str
        del self.result

if __name__ == "__main__":
    unittest.main()
