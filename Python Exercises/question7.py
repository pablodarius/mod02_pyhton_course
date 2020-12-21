import unittest

# Return the total count of sub-string “Emma” appears in the given string

def count_word(word, sentence):
    return sentence.count(word)

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.word = "Emma"
        self.sentence = "Emma is good developer. Emma is a writer"
        self.count = 2

    def test01(self):
        self.assertEqual(count_word(self.word, self.sentence), self.count)

    def tearDown(self):
        print("Deleting context...")
        del self.word
        del self.sentence
        del self.count

if __name__ == "__main__":
    unittest.main()
