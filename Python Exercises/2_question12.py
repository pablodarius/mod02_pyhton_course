import unittest

# Display Fibonacci series up to 10 terms

def fibonacci(terms):
    prev1, prev2 = 0, 1
    counter = 0
    while counter < terms:
        print(prev1, end=" ")
        aux = prev1 + prev2
        prev1 = prev2
        prev2 = aux
        counter += 1
    
class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.terms = 10

    def test01(self):
        fibonacci(self.terms)

    def tearDown(self):
        print("Deleting context...")
        del self.terms

if __name__ == "__main__":
    unittest.main()
