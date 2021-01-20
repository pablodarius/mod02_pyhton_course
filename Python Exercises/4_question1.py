import unittest

# Given a Python list you should be able to display Python list in the following order

def sorted_list(input_list):
    input_list.sort(reverse=True)
    # input_list = input_list[::-1]
    return input_list

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.input_list = [100, 200, 300, 400, 500]
        self.result = [500, 400, 300, 200, 100]

    def test01(self):
        self.assertEqual(sorted_list(self.input_list), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.input_list
        del self.result

if __name__ == "__main__":
    unittest.main()
