import unittest

# Display the cube of the number up to a given integer

def digits_cube(number):
    for n in range(1, number + 1):
        print("Current Number is : {}  and the cube is {}".format(n, n**3))

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.number = 6

    def test01(self):
        digits_cube(self.number)

    def tearDown(self):
        print("Deleting context...")
        del self.number

if __name__ == "__main__":
    unittest.main()
