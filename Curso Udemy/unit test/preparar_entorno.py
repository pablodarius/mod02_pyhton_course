import unittest

# test fixture o accesorios de prueba (preprar el entorno y limpieza para dejarlo como estaba) setUp (conectarse a servidor, bbdd...) y tearDown(dejarlo todo ok) respectivamente

def doblar(a): return a*2

class PruebaTestFixture(unittest.TestCase):
    def setUp(self):
        print("Preparando el contexto")
        self.numeros = [1, 2, 3, 4, 5]
    
    def test(self):
        print("Realizando pruebas")
        r = [doblar(n) for n in self.numeros]
        self.assertEqual(r, [2, 4, 6, 8, 10])
    
    def tearDown(self):
        print("Destruyendo el contexto")
        del(self.numeros)

if __name__ == "__main__":
    unittest.main()