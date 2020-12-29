import unittest

# Imprime los primeros 10 números naturales usando el bucle while

def print_number(top):
    number = 0
    while top > 0:
        print(number)
        number += 1
        top -= 1

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.top = 10

    def test01(self):
        print_number(self.top)

    def tearDown(self):
        print("Deleting context...")
        del self.top


if __name__ == "__main__":
    unittest.main()
