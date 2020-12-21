import unittest

# Print downward Half-Pyramid Pattern with Star (asterisk)

def pyramid(number):
    for i in range(number):
        print("*", end=" ")
    print("\b")
    if number != 0:
        pyramid(number-1)

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.number = 10

    def test01(self):
        pyramid(self.number)

    def tearDown(self):
        print("Deleting context...")
        del self.number

if __name__ == "__main__":
    unittest.main()
