import unittest

# Realizar un algoritmo que permita leer dos valores, determinar cual de los dos valores es el menor y escríbalo

def smallest(a, b):
    if a < b:
        result = "The smallest is A: %s" % (a)
    else:    
        result = "The smallest is B: %s" % (b)    
    return result

A = 0
B = 0
while A==B:
    A = input("Introduce a number: ")
    B = input("Introduce another number: ")

print(smallest(A,B))


class testing(unittest.TestCase):    
    def test01(self):
        self.assertEqual(smallest(1, 2), "The smallest is A: 1")
    
    def test02(self):
        self.assertEqual(smallest(2, 1), "The smallest is B: 1")

if __name__ == "__main__":
    unittest.main()