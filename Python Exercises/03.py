import unittest

# Desarrolle un algoritmo que realice la sumatoria de los números enteros comprendidos entre dos números dados
# Desarrolle un algoritmo que realice la sumatoria de los números enteros múltiplos de 5, comprendidos entre el 1 y el 100, es decir, 5 + 10 + 15 +…. + 100 
# Desarrolle un algoritmo que realice la sumatoria de los números enteros pares comprendidos entre el 1 y el 100, es decir, 2 + 4 + 6 +…. + 100
# Desarrolle un algoritmo que lea los primeros 300 números enteros y determine cuántos de ellos son impares, al final deberá indicar su sumatoria


def summatory(a,b):
    result = 0
    for n in range(a, b+1):
        result += n

    return result

def summatory5(a,b):
    result = 0
    for n in range(a, b+1, 5):
        #print(n)
        result += n

    return result

def summatoryEven(a,b):
    result = 0
    for n in range(a, b+1, 2):
        #print(n)
        result += n

    return result

def howMuchOdd(a,b):
    result = 0
    for n in range(a, b+1):
        if n%2 != 0:
            #print(n)
            result += 1

    return result

class testing(unittest.TestCase):    
    def test01(self):
        self.assertEqual(summatory(1, 100), 5050)

    def test02(self):
        self.assertEqual(summatory5(0, 100), 1050)

    def test03(self):
        self.assertEqual(summatoryEven(0, 100), 2550)

    def test04(self):
        self.assertEqual(howMuchOdd(0, 300), 150)

if __name__ == "__main__":
    unittest.main()
