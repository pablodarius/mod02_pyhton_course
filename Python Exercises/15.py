import unittest

# Desarrolle un algoritmo que permita determinar a partir de un número de días, ingresado por pantalla, ¿Cuántos
# años, meses, semanas y días; constituyen el número de días proporcionado

def daysTime(numDays):
    years = round(numDays / 365)
    months = round(numDays / 30)
    weeks = round(numDays / 7)
    return [years, months, weeks]


class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.catTime = [1, 12, 52]

    def test01(self):
        self.assertEqual(daysTime(365), self.catTime)

    def tearDown(self):
        print("Deleting context...")
        del self.catTime

if __name__ == "__main__":
    unittest.main()