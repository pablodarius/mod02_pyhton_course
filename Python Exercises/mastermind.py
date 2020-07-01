#Programa para jugar con la compu-tadora: elMastermind. El Mastermind es un juego que consiste en 
# deducir un código numéricode (por ejemplo) cuatro cifras.
import unittest
import random

NUMBERS = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

def generateCode():
    code = set()
    while len(code) != 4:
        code.add(random.choice(NUMBERS))    
    return code

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")        

    def test_initialRandom(self):
        self.assertEqual(len(generateCode()), 4)
    
    def test_differentNums(self):
        self.assertEqual(len(generateCode()), 4)

    def tearDown(self):
        print("Deleting context...")       


if __name__ == "__main__":
    unittest.main()