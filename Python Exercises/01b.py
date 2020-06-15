import unittest

# Realizar un algoritmo que sume dos números

def sum(a, b):    
    return (a+b)

A = int(input("Introduce a number: "))
B = int(input("Introduce another number: "))
print(sum(A,B))

class testing(unittest.TestCase):    
    def test01(self):
        self.assertEqual(sum(1, 2), 3)
    
    def test02(self):
        self.assertEqual(sum(1, -2), -1)

if __name__ == "__main__":
    unittest.main()