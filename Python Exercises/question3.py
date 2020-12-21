import unittest

# Given a string, display only those characters which are present at an even index number

def even_index(word):    
    for i in range(0, len(word)-1, 2):
        print(word[i])

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.word = "potatoes"

    def test01(self):
        print("Orginal String is {}".format(self.word))
        print("Printing only even index chars")
        even_index(self.word)

    def tearDown(self):
        print("Deleting context...")
        del self.word


if __name__ == "__main__":
    unittest.main()
