import unittest

# Realice un algoritmo que a partir de proporcionarle la velocidad de un automóvil, expresada en kilómetros por hora, proporcione la velocidad en metros por segundo

def convertToMS(vel):
    return round((vel * 1000) / 3600, 2)

def convertToKM(vel):
    return round((vel * 3600) / 1000, 2)    

class testing(unittest.TestCase):
    def test01(self):
        self.assertEqual(convertToMS(100), 27.78)    
    
    def test02(self):
        self.assertEqual(convertToKM(100), 360)
    
if __name__ == "__main__":
    unittest.main()