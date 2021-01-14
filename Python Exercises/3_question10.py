import unittest

# Given an input string, count occurrences of all characters within a string

def cout_ocurrences(input_str):
    result = dict()
    for i in input_str:
        count = input_str.count(i)
        result[i] = count
    return result

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str = "Apple"
        self.result = {'A': 1, 'p': 2, 'l': 1, 'e': 1}

    def test01(self):
        self.assertEqual(cout_ocurrences(self.str), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.str
        del self.result

if __name__ == "__main__":
    unittest.main()
