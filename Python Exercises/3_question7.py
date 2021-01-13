import unittest

# String characters balance Test, all the chars in the s1 are there in s2

def balanced_string(s1, s2):
    flag = True
    for s in s1:
        if s not in s2:
            flag = False

    return flag

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str1 = "Yen"
        self.str2 = "Ynf"
        self.str3 = "PYnative"

    def test01_balanced(self):
        self.assertTrue(balanced_string(self.str1, self.str3))
    
    def test02_not_balanced(self):
        self.assertFalse(balanced_string(self.str2, self.str3))

    def tearDown(self):
        print("Deleting context...")
        del self.str1
        del self.str2
        del self.str3

if __name__ == "__main__":
    unittest.main()
