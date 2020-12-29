import unittest

# Imprime la tabla de multiplicar del número dado

def multiplication_table(number):
    for i in range(1, 11):
        print("{} x {} = {}".format(i, number, i*number))

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.number = 10

    def test01(self):
        multiplication_table(self.number)

    def tearDown(self):
        print("Deleting context...")
        del self.number


if __name__ == "__main__":
    unittest.main()
