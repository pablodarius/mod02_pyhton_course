import unittest

# Given a string and an integer number n,
# remove characters from a string starting from zero up to n and return a new string

def cut_string(word, n):
    return word[n:]

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.word = "potatoes"
        self.number = 3
        self.result = "atoes"
        self.number_wrong = 9
        self.empty = ""

    def test01_OK(self):
        self.assertEqual(cut_string(self.word, self.number), self.result)

    def test02_Wrong(self):
        self.assertEqual(cut_string(self.word, self.number_wrong), self.empty)

    def tearDown(self):
        print("Deleting context...")
        del self.word
        del self.number
        del self.number_wrong
        del self.result
        del self.empty

if __name__ == "__main__":
    unittest.main()
