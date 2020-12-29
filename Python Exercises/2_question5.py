import unittest

# Dada una lista, iterarla y mostrar números que son divisibles por 5 
# y si encuentra un número mayor que 150, detenga la iteración del ciclo.

def five_multiples_minor_hundred_fifty(numbers):
    result = []
    for n in numbers:
        if (n % 5 == 0) and (n <= 150):
            result.append(n)
    return result

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.numbers = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
        self.result = [15,55,75,150]

    def test01(self):
        self.assertEqual(five_multiples_minor_hundred_fifty(self.numbers), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.numbers
        del self.result


if __name__ == "__main__":
    unittest.main()
