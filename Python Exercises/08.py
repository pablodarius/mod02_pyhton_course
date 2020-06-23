import unittest

# Desarrolle un algoritmo que permita convertir calificaciones numéricas, según la siguiente tabla:
# A = 19 y 20, B =16, 17 y 18, C = 13, 14 y 15, D = 10, 11 y 12, E = 1 hasta el 9. Se asume que la nota está comprendida entre 1 y 20

def sortNumbers(a, b):
    result = []
    result.append(a)
    result.append(b)
    result = sorted(result)

    return result

def sortNumbers_2(numbers):    
    numbers = sorted(numbers)

    return numbers

class testing(unittest.TestCase):
    def test01(self):
        self.assertEqual(sortNumbers(5, 1), [1, 5])
    
    def test02(self):
        self.assertEqual(sortNumbers_2([5, 1, 3, 9, 6, 2, 8, 4, 7]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == "__main__":
    unittest.main()