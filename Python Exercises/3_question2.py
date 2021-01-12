import unittest

# Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1

def add_in_middle(s1, s2):
    middle = len(s1) // 2
    result = s1[:middle] + s2 + s1[middle:]
    return result

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str1 = "Ault"
        self.str2 = "Kelly"
        self.result = "AuKellylt"

    def test01(self):
        self.assertEqual(add_in_middle(self.str1, self.str2), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.str1
        del self.str2
        del self.result

if __name__ == "__main__":
    unittest.main()
