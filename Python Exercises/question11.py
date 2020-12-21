import unittest

# Write a code to extract each digit from an integer, in the reverse order

def reverse_number(number):
    number = str(number)[::-1]
    for n in number:
        print(n, end=" ")

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.number = 7536

    def test01(self):
        reverse_number(self.number)

    def tearDown(self):
        print("Deleting context...")
        del self.number

if __name__ == "__main__":
    unittest.main()
