import unittest

# Given a range of first 10 numbers, Iterate from start number to the end number
# and print the sum of the current number and previous number

def range_sums(r):
    previous = 0
    for num in range(r):
        sum = num + previous    
        print("Current Number {} Previous Number {} Sum: {}".format(num, previous, sum))
        previous = num


class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")


    def test01(self):
        print("Printing current and previous number sum in a given range(10)")
        range_sums(10)

    def tearDown(self):
        print("Deleting context...")


if __name__ == "__main__":
    unittest.main()
