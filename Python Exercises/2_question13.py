import unittest

# Write a loop to find the factorial of any number

def factorial_loop(number):
    if number < 0:
        return False
    elif number == 0:
        return 1
    else:
        result = 1
        for n in range(1, number + 1):
            result *= n
        return result
    
class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.right_number = 5
        self.wrong_number = -5
        self.zero = 0
        self.right_result = 120
        self.zero_result = 1

    def test01_right(self):
        self.assertEqual(factorial_loop(self.right_number), self.right_result)
    
    def test02_wrong(self):
        self.assertFalse(factorial_loop(self.wrong_number))
    
    def test03_zero(self):
        self.assertEqual(factorial_loop(self.zero), self.zero_result)

    def tearDown(self):
        print("Deleting context...")
        del self.right_number
        del self.wrong_number
        del self.zero
        del self.right_result
        del self.zero_result

if __name__ == "__main__":
    unittest.main()
