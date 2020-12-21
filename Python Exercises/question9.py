import unittest

# Reverse a given number and return true if it is the same as the original number

def is_same(ori_number):
    ori_number = str(ori_number)
    final_number = ori_number[::-1]
    print(final_number)
    return ori_number == final_number

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.number = 123456
        self.number_same = 123321

    def test01_SAME(self):
        self.assertTrue(is_same(self.number_same))

    def test02_NOT_SAME(self):
        self.assertFalse(is_same(self.number))

    def tearDown(self):
        print("Deleting context...")
        del self.number
        del self.number_same

if __name__ == "__main__":
    unittest.main()
