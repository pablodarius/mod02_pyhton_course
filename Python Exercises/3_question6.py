import unittest

# Given two strings, s1 and s2, create a mixed String

def mixed_string(s1, s2):
    result = ""
    length_s1 = len(s1)
    length_s2 = len(s2)
    s2 = s2[::-1]
    length = length_s1 if length_s1 > length_s2 else length_s2
    for i in range(0, length):
        if i < length_s1:
            result += s1[i]
        if i < length_s2:
            result += s2[i]
    return result

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str1 = "Abcd"
        self.str2 = "Xyz"
        self.result = "AzbycXd"

    def test01(self):
        self.assertEqual(mixed_string(self.str1, self.str2), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.str1
        del self.str2
        del self.result

if __name__ == "__main__":
    unittest.main()
