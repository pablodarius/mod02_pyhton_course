import unittest

#Given a two integer numbers return their product and if the product is greater than 1000, return their sum

def multiplication_or_sum(n1, n2):
    top = 1000
    multiplication = n1 * n2

    if multiplication <= top:
        result = multiplication
    else:
        result = n1 + n2

    return result

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.num1 = 20
        self.num2 = 30
        self.num3 = 40
        self.result_greater = 70
        self.result_not_greater = 600

    def test01_not_greater(self):
        print("test01_not_greater...")
        result = multiplication_or_sum(self.num1, self.num2)
        print("The result is {}".format(result))
        self.assertEqual(result, self.result_not_greater)
    
    def test02_is_greater(self):
        print("test02_is_greater...")
        result = multiplication_or_sum(self.num2, self.num3)
        print("The result is {}".format(result))
        self.assertEqual(result, self.result_greater)

    def tearDown(self):
        print("Deleting context...")
        del self.num1
        del self.num2
        del self.num3
        del self.result_greater
        del self.result_not_greater

if __name__ == "__main__":
    unittest.main()
