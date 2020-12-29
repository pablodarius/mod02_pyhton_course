import unittest

# Imprima el siguiente patrón
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

def print_pyramid(top):
    counter = 1
    while counter <= top:
        number = 1
        while number <= counter:
            print(number, end=" ")
            number += 1
        print("\b")
        counter += 1

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.top = 5

    def test01(self):
        print_pyramid(self.top)

    def tearDown(self):
        print("Deleting context...")
        del self.top


if __name__ == "__main__":
    unittest.main()
