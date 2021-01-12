import unittest

#  Given 2 strings, s1, and s2 return a new string made of the first, middle and last char each input string

def add_ini_middle_fin(s1, s2):
    result = ""
    result += s1[0] + s2[0]
    result += s1[len(s1) // 2] + s2[len(s2) // 2]
    result += s1[-1] + s2[-1]
    return result

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str1 = "America"
        self.str2 = "Japan"
        self.result = "AJrpan"

    def test01(self):
        self.assertEqual(add_ini_middle_fin(self.str1, self.str2), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.str1
        del self.str2
        del self.result

if __name__ == "__main__":
    unittest.main()
