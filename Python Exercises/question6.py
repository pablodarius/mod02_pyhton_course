import unittest

# Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

def five_multiples(numbers):
    for n in numbers:
        if n % 5 == 0: print(n)

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.numbers = [10, 20, 33, 46, 55]

    def test01(self):
        print("The list of numbers is: {}".format(self.numbers))
        print("And the multiples of 5 are:")
        five_multiples(self.numbers)

    def tearDown(self):
        print("Deleting context...")
        del self.numbers

if __name__ == "__main__":
    unittest.main()
