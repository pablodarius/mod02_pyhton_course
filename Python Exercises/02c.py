import unittest

# Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las variables A, B, y C respectivamente. 
# El algoritmo debe indicar cual es el menor. Asumiendo que los tres valores introducidos por el teclado son valores distintos

def smallest(a,b,c):
    if (a < b and a < c):
        result = "The smallest is A: %s" % (a)
    elif (b < c):
        result = "The smallest is B: %s" % (b)
    else:
        result = "The smallest is C: %s" % (c)
    return result

A = 0
B = 0
C = 0
while (A == B or A == C or B == C):
    A = input("Introduce a number: ")
    B = input("Introduce another number: ")
    C = input("Introduce the last number: ")
    if (A == B or A == C or B == C):
        print("The three numbers must be different.")

print(smallest(A,B,C))


class testing(unittest.TestCase):    
    def test01(self):
        self.assertEqual(smallest(1, 2, 3), "The smallest is A: 1")
    
    def test02(self):
        self.assertEqual(smallest(4, 3, 2), "The smallest is C: 2")
    
    def test03(self):
        self.assertEqual(smallest(3, 1, 2), "The smallest is B: 1")

if __name__ == "__main__":
    unittest.main()
