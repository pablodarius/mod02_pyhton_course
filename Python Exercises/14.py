import unittest

# Desarrolle un algoritmo que funcione como caja registradora, recibir productos (codigo y precio) y emitir precio total con iva 21%

def ckeckout(products):
    IVA = 0.21
    prices = products.values()
    total = 0
    for p in prices:
        total += p
    total += total * IVA
    return total


class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.products = {'Shoes': 100, 'Jacket': 60, 'Trousers': 39, 'Waistcoats': 19, 'Tie': 15, 'Dress_shirt': 42}

    def test01(self):
        self.assertEqual(ckeckout(self.products), 332.75)

    def tearDown(self):
        print("Deleting context...")
        del self.products

if __name__ == "__main__":
    unittest.main()