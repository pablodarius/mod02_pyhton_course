import unittest

# Split a given string on hyphens into several substrings and display each substring

def find_last_position(input_string):
    output = input_string.split("-")
    for s in output:
        print(s)

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str = "Emma-is-a-data-scientist"

    def test01(self):
        find_last_position(self.str)

    def tearDown(self):
        print("Deleting context...")
        del self.str

if __name__ == "__main__":
    unittest.main()
