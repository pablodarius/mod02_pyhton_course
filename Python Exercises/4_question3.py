import unittest

# Given a Python list. Turn every item of a list into its square

def square_list(l1):
    result = [x**2 for x in l1]
    return result

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.input_list = [1, 2, 3, 4, 5, 6, 7]
        self.result = [1, 4, 9, 16, 25, 36, 49]

    def test01(self):
        self.assertEqual(square_list(self.input_list), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.input_list
        del self.result

if __name__ == "__main__":
    unittest.main()
