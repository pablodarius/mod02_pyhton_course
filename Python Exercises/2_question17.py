import unittest

# Find the sum of the series 2 +22 + 222 + 2222 + .. n terms

def two_sum_terms(number):
    result = 0
    for n in range(1, number + 1):
        sum = ""
        for i in range(0, n):
            sum += "2"
        result += int(sum)
    return result

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.number = 5
        self.result = 24690

    def test01(self):
        self.assertEqual(two_sum_terms(self.number), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.number
        del self.result

if __name__ == "__main__":
    unittest.main()
