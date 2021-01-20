import unittest

# Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order

def show_lists_reverse(l1, l2):
    for x, y in zip(l1,l2[::-1]):
        print(x, y)

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.input_list1 = [10, 20, 30, 40]
        self.input_list2 = [100, 200, 300, 400]
        
    def test01(self):
        show_lists_reverse(self.input_list1, self.input_list2)

    def tearDown(self):
        print("Deleting context...")
        del self.input_list1
        del self.input_list2

if __name__ == "__main__":
    unittest.main()
