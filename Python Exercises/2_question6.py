import unittest

# Dado un número, cuente el número total de dígitos de un número

def digit_counter(number):
    counter = 0
    digits = str(number)
    for d in digits:
        counter += 1
    return counter

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.number = 75869
        self.result = 5

    def test01(self):
        self.assertEqual(digit_counter(self.number), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.number
        del self.result


if __name__ == "__main__":
    unittest.main()
