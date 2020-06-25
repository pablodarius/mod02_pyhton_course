import unittest
import datetime
import math

# Realice un algoritmo que calcule el monto a pagar por el servicio de estacionamiento, teniendo en cuenta que por la primera hora de estadía
# se tiene una tarifa de 1000 bolívares y las restantes tienen un costo de 600 bolívares. Se tiene como datos: hora de entrada,
# hora de salida (formato militar), iniciada una hora se contabiliza como hora total.

def paySER(enter, out):
    if out > enter:
        time = out - enter
        hoursParking = math.ceil(time.seconds / 3600)    
    
        return 1000 + (600 * (hoursParking - 1))
    else:
        return -1

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.park = datetime.timedelta(hours=7, minutes=30, seconds=00)
        self.leave = datetime.timedelta(hours=9, minutes=39, seconds=00)

    def test01(self):
        self.assertEqual(paySER(self.park, self.leave), 2200)
    
    def test01_error_01(self):
        self.assertEqual(paySER(self.leave, self.park), -1)
    
    def test01_error_02(self):
        self.assertEqual(paySER(self.park, self.park), -1)

    def tearDown(self):
        print("Deleting context...")
        del self.park
        del self.leave

if __name__ == "__main__":
    unittest.main()