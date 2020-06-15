import unittest

# Desarrolle un algoritmo que permita leer dos valores distintos, determinar cual de los dos valores es el mayor y escribirlo

def greater(a, b):
    if a > b:
        result = "The greater is A: %s" % (a)
    else:    
        result = "The greater is B: %s" % (b)    
    return result

A = 0
B = 0
while A==B:
    A = input("Introduce a number: ")
    B = input("Introduce another number: ")
    
print(greater(A, B))


class testing(unittest.TestCase):    
    def test01(self):
        self.assertEqual(greater(1, 2), "The greater is B: 2")
    
    def test02(self):
        self.assertEqual(greater(2, 1), "The greater is A: 2")

if __name__ == "__main__":
    unittest.main()