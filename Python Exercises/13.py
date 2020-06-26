import unittest

# Desarrolle un algoritmo para la empresa Constructora Tecnovivir Casas C.A., que le permita calcular e imprimir
# la nómina para su cancelación a un total de 50 obreros calificados a quienes debe cancelar por horas trabajadas. La hora trabajada se pautó en 30.000 Bolívares.

def workersHours(hours):
    total = 0
    for h in hours:
        total += h * 30

    return total


class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.hours = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.hoursReal = [40, 40, 40, 40, 48, 40, 40, 40, 40, 40, 40, 40, 40, 
        40, 40, 40, 43, 40, 40, 40, 40, 32, 40, 40, 40, 40, 40, 20, 40, 40, 40, 
        40, 40, 40, 40, 40, 40, 40, 40, 40, 42, 40, 40, 40, 40, 40, 40, 40, 40, 40]

    def test01(self):
        self.assertEqual(workersHours(self.hours), 1500)
    
    def test02(self):
        self.assertEqual(workersHours(self.hoursReal), 59550)

    def tearDown(self):
        print("Deleting context...")
        del self.hours
        del self.hoursReal

if __name__ == "__main__":
    unittest.main()