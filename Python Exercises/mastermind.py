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

def checkAttempt(code, attempt):
    coincidence = 0
    success = 0
    for a in attempt:
        if a in code:
            coincidence += 1
            if list(code).index(a) == list(attempt).index(a):
                success += 1
    return coincidence, success

def letsPlay():
    numberAttempts = 10
    won = False
    code = generateCode()

    while numberAttempts > 0 and won != True:
        userCode = []
        print("Guess our four numbers code...")
        n = input("First Number: ")
        userCode.append(n)
        n = input("Second Number: ")
        userCode.append(n)
        n = input("Third Number: ")
        userCode.append(n)
        n = input("Fourth Number: ")
        userCode.append(n)

        result = checkAttempt(code, userCode)        
        if  result != (4, 4):
            print("Nope! Try again: {} Coincidences, {} Success".format(result[0], result[1]))
            numberAttempts -= 1
        else:
            won = True
        print("***********************************************************")
    
    if won:
        print("Cool, You win!!! :)")
        return True
    else:
        print("Ohhhhh, sorry you lose!!! :(")
        return False

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")              

    def test_initialRandom(self):        
        self.assertEqual(len(generateCode()), 4)
    
    def test_checking(self):
        code = generateCode()     
        self.assertEqual(checkAttempt(code, code), (4, 4))
    
    def test_play(self):
        self.assertTrue(letsPlay())

    def tearDown(self):
        print("Deleting context...")


if __name__ == "__main__":
    unittest.main()