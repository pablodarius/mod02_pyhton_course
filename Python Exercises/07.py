import unittest

# Desarrolle un algoritmo que permita convertir calificaciones numéricas, según la siguiente tabla:
# A = 19 y 20, B =16, 17 y 18, C = 13, 14 y 15, D = 10, 11 y 12, E = 1 hasta el 9. Se asume que la nota está comprendida entre 1 y 20

def califications(calif):
    results = []

    for c in calif:
        if c >= 1 and c <= 9:
            results.append('E')
        elif c >= 10 and c <= 12:
            results.append('D')
        elif c >= 13 and c <= 15:
            results.append('C')
        elif c >= 16 and c <= 18:
            results.append('B')
        elif c >= 19 and c <= 20:
            results.append('A')

    return results

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.calif = [20, 5, 16, 13, 17, 19, 2, 10, 8, 6]

    def test01(self):
        self.assertEqual(califications(self.calif), ['A', 'E', 'B', 'C', 'B', 'A', 'E', 'D', 'E', 'E'])

    def tearDown(self):
        print("Deleting context...")
        del(self.calif)

if __name__ == "__main__":
    unittest.main()