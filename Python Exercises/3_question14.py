import unittest

# Remove empty strings from a list of strings

def remove_empty(str_list):
    result = list(filter(None, str_list))
    return result

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str_list = ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']
        self.result_list = ['Emma', 'Jon', 'Kelly', 'Eric']

    def test01(self):
        self.assertEqual(remove_empty(self.str_list), self.result_list)

    def tearDown(self):
        print("Deleting context...")
        del self.str_list
        del self.result_list

if __name__ == "__main__":
    unittest.main()
