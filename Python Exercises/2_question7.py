import unittest

# Imprima el siguiente patrón usando el bucle for
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

def reverse_pyramid(number):
    for n in range(number, 0, -1):
        for i in range(n, 0, -1):
            print(i, end=" ")
        print("\b") 

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.number = 5

    def test01(self):
        reverse_pyramid(self.number)

    def tearDown(self):
        print("Deleting context...")
        del self.number

if __name__ == "__main__":
    unittest.main()
