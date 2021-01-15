import unittest

# Find the last position of a substring “Emma” in a given string

def find_last_position(input_string, substring):
    return input_string.rfind(substring)

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str = "Emma is a data scientist who knows Python. Emma works at google."
        self.substr = "Emma"
        self.result = 43

    def test01(self):
        self.assertEqual(find_last_position(self.str, self.substr), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.str
        del self.substr
        del self.result

if __name__ == "__main__":
    unittest.main()
