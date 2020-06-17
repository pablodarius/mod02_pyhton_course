import unittest
import math

# Determinar la hipotenusa de un triángulo rectángulo conocidas las longitudes de sus dos catetos
# Desarrollar un algoritmo que calcule el área de un cuadrado

def hypotenuse(a,b):
    if (a > 0 and b > 0):
        a = a**2
        b = b**2
        result = a + b
        return math.sqrt(result)    
    else:
        return -1

def rectangleArea(a,b):
    if (a > 0 and b > 0):        
        return a * b    
    else:
        return -1

class testing(unittest.TestCase):    
    def test01(self):
        self.assertEqual(hypotenuse(3, 4), 5)
    
    def test01_Error_1(self):
        self.assertEqual(hypotenuse(-3, 4), -1)
    
    def test01_Error_2(self):
        self.assertEqual(hypotenuse(3, -4), -1)
    
    def test02(self):
        self.assertEqual(rectangleArea(6, 3), 5)
    
    def test02_Error_1(self):
        self.assertEqual(rectangleArea(-6, 3), -1)
    
    def test02_Error_2(self):
        self.assertEqual(rectangleArea(6, -3), -1)
    

if __name__ == "__main__":
    unittest.main()
