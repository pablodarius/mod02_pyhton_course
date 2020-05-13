import unittest

def doblar(a): return a*2
def sumar(a,b): return a+b
def espar(a): return True if a%2 ==0 else False

class PruebasFunciones(unittest.TestCase):
    # def test(self):
        # pass (respuesta OK)
        # raise AssertionError() (respuesta FAIL)
        # 1/0 # (respuesta ERROR)
    
    def test_doblar(self):
        self.assertEqual(doblar(10), 20)
        self.assertEqual(doblar('Ab'), 'AbAb')
    
    def test_sumar(self):
        self.assertEqual(sumar(-15,15), 0)
        self.assertEqual(sumar('Ab','cd'), 'Abcd')
        self.assertEqual(sumar('Ab', 0), 'Ab0')

    def test_espar(self):
        self.assertEqual(espar(11), False)
        self.assertEqual(espar(68), True)
        self.assertEqual(espar(69), True)    

if __name__ == "__main__":
    unittest.main()