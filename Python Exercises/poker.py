# Genera una mano de 4 cartas de la baraja frnacesa y comprueba si el jugador tiene poker
import unittest
import random

NUMBERS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING')
#NUMBERS = ('1', '2')
TYPES = ('CLUBS', 'HEARTS', 'SPADES', 'DIAMONDS')

def generateHand():
    hand = set()
    while len(hand) != 4:
        hand.add((random.choice(NUMBERS), random.choice(TYPES)))
    return hand

def checkHand(hand):
    print("Your hand:")
    poker = True
    nums = []
    for h in hand:
        print(F"{h[0]}\tof\t{h[1]}")
        if len(nums) == 0:
            nums.append(h[0])
        elif h[0] not in nums:
            poker = False
    return poker

class testing(unittest.TestCase):
    def test_checking(self):
        yourHand = generateHand()
        self.assertEqual(checkHand(yourHand), True)

if __name__ == "__main__":
    unittest.main()