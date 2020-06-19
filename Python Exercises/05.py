import unittest
import math

# Desarrolle un algoritmo que permita determinar el área y volumen de un cilindro dado su radio (R) y altura (H)

def rectangleArea(a,b):
    if (a > 0 and b > 0):
        return a * b
    else:
        return -1

def cylinderArea(r,h):
    if (r > 0 and h > 0):
        result = (2 * math.pi * r**2) + h * (2 * math.pi * r)
        return round(result, 2)
    else:
        return -1

class testing(unittest.TestCase):
    def test01(self):
        self.assertEqual(rectangleArea(6, 3), 18)
    
    def test01_Error_1(self):
        self.assertEqual(rectangleArea(-6, 3), -1)
    
    def test01_Error_2(self):
        self.assertEqual(rectangleArea(6, -3), -1)

    def test02(self):
        self.assertEqual(cylinderArea(2, 6), 100.53)
    
    def test02_Error_1(self):
        self.assertEqual(cylinderArea(-2, 6), -1)
    
    def test02_Error_2(self):
        self.assertEqual(cylinderArea(2, -6), -1)    

if __name__ == "__main__":
    unittest.main()