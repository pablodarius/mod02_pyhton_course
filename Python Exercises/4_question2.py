import unittest

# Concatenate two lists index-wise

def combined_list(l1, l2):
    result = [i + j for i, j in zip(l1, l2)]
    return result

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.input_list1 = ["M", "na", "i", "Ke"]
        self.input_list2 = ["y", "me", "s", "lly"]
        self.result = ['My', 'name', 'is', 'Kelly']

    def test01(self):
        self.assertEqual(combined_list(self.input_list1, self.input_list2), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.input_list1
        del self.input_list2
        del self.result

if __name__ == "__main__":
    unittest.main()
