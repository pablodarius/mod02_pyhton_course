import unittest

# Given a list of numbers, return True if first and last number of a list is same

def same_ini_fin(numbers):
    return numbers[0] == numbers [-1]

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.same = [10, 20, 30, 40, 10]
        self.not_same = [10, 20, 30, 40, 50]

    def test01_OK(self):
        self.assertTrue(same_ini_fin(self.same))
    
    def test02_NOT_OK(self):
        self.assertFalse(same_ini_fin(self.not_same))

    def tearDown(self):
        print("Deleting context...")
        del self.same
        del self.not_same

if __name__ == "__main__":
    unittest.main()
