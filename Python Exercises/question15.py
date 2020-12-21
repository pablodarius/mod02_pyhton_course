import unittest

# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp

def exponent(base, exp):
    result = base
    for i in range(exp - 1):
        result *= base
    return result

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.base = 5
        self.exp = 4
        self.result = 625

    def test01(self):
        self.assertEqual(exponent(self.base, self.exp), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.base
        del self.exp
        del self.result


if __name__ == "__main__":
    unittest.main()
