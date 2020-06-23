import unittest

# Recibir un número y determinar si es primo
# Recibir un número sacar la lista de todos los primmos menores a ese número

def primeNumber(a):
    if a > 1:
        for n in range(a-1, 1, -1):
            if a % n == 0:
                return False
    else:
        return -1

    return True

def primesList(a):
    primes = []
    for n in range(2, a+1):
        if (n > 1 and primeNumber(n)):
            primes.append(n)

    return primes


class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.primes = [2, 3, 5, 7, 11]
        self.empty = []

    def test01(self):
        self.assertEqual(primeNumber(9973), True)

    def test01_error(self):
        self.assertEqual(primeNumber(-7), -1)

    def test02(self):
        self.assertEqual(primesList(11), self.primes)
    
    def test02_error(self):
        self.assertEqual(primesList(-11), self.empty)

    def tearDown(self):
        print("Deleting context...")
        del self.primes
        del self.empty

if __name__ == "__main__":
    unittest.main()