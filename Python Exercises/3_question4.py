import unittest

# Arrange string characters such that lowercase letters should come first

def lowercase_first(s1):
    upper = ""
    lower = ""
    for s in s1:
        if s.islower():
            lower += s
        if s.isupper():
            upper += s

    return lower + upper

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str1 = "PyNaTive"
        self.result = "yaivePNT"

    def test01(self):
        self.assertEqual(lowercase_first(self.str1), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.str1
        del self.result

if __name__ == "__main__":
    unittest.main()
