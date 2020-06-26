import unittest

# Desarrolle un algoritmo que permita calcular Promedio de Notas

def averageCalif(calif):
    average = 0
    for c in calif:
        average += c

    return round(average/len(calif), 2)


class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.califications = [10, 2, 38, 23, 38, 23, 21]

    def test01(self):
        self.assertEqual(averageCalif(self.califications), 22.14)

    def tearDown(self):
        print("Deleting context...")
        del self.califications

if __name__ == "__main__":
    unittest.main()