import unittest

# Desarrolle un algoritmo que permita leer tres valores y almacenarlos en las variables A, B, y C respectivamente. 
# El algoritmo debe indicar cual es el mayor. Asumiendo que los tres valores introducidos por el teclado son valores distintos

def greater(a,b,c):
    if (a > b and a > c):
        result = "The greater is A: %s" % (a)
    elif (b > c):
        result = "The greater is B: %s" % (b)
    else:
        result = "The greater is C: %s" % (c)
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

print(greater(A,B,C))


class testing(unittest.TestCase):    
    def test01(self):
        self.assertEqual(greater(1, 2, 3), "The greater is C: 3")
    
    def test02(self):
        self.assertEqual(greater(1, 3, 2), "The greater is B: 3")
    
    def test03(self):
        self.assertEqual(greater(3, 1, 2), "The greater is A: 3")

if __name__ == "__main__":
    unittest.main()
