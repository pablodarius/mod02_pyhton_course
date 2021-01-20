import unittest

# Concatenate two lists in the following order

def mixed_words_list(l1, l2):
    result = [x + y for x in l1 for y in l2]
    return result

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.input_list1 = ["Hello ", "take "]
        self.input_list2 = ["Dear", "Sir"]
        self.result = ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
        
    def test01(self):
        self.assertEqual(mixed_words_list(self.input_list1, self.input_list2), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.input_list1
        del self.input_list2
        del self.result

if __name__ == "__main__":
    unittest.main()
