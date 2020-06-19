import unittest
import math

# Desarrolle un algoritmo que permita leer un valor cualquiera N y escriba si dicho número es par o impar
# Desarrolle un algoritmo que le permita determinar de una lista de números:
#   b.1. ¿Cuántos están entre el 50 y 75, ambos inclusive?
#   b.2. ¿Cuántos mayores de 80?
#   b.3. ¿Cuántos menores de 30?

def even_or_odd(a):
    if (a % 2 == 0):
        return "even"
    else:
        return "odd"

def numbersRange(numbers):
    r1 = 0 # 50-75
    r2 = 0 # >80
    r3 = 0 # <30

    for n in numbers:        
        if (n >= 50 and n <=75):
            r1 += 1
        elif (n > 80):
            r2 += 1
        elif (n < 30 and n <=75):
            r3 += 1
        
    return [r1, r2, r3]

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.numbers = [1, 5, 89, 63, 54, 75, 25, 66, 84, 32, 89, 21, 45, 63, 47]

    def test01_1(self):
        self.assertEqual(even_or_odd(3), "odd")
    
    def test01_2(self):
        self.assertEqual(even_or_odd(2), "even")
    
    def test01_3(self):
        self.assertEqual(even_or_odd(-3), "odd")
    
    def test01_4(self):
        self.assertEqual(even_or_odd(-2), "even")
    
    def test02(self):
        self.assertEqual(numbersRange(self.numbers), [5, 3, 4])
    
    def tearDown(self):
        print("Deleting context...")
        del(self.numbers)


if __name__ == "__main__":
    unittest.main()