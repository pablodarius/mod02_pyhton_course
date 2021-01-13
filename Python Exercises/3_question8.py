import unittest

# Find all occurrences of “USA” in given string ignoring the case

def ocurrences(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    return s1.count(s2)

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str1 = "Welcome to USA. usa awesome, isn't it?"
        self.str2 = "USA"
        self.result = 2

    def test01(self):
        self.assertEqual(ocurrences(self.str1, self.str2), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.str1
        del self.str2
        del self.result

if __name__ == "__main__":
    unittest.main()
