import unittest

# Desarrolle un algoritmo que lea cuatro números diferentes y a continuación imprima el mayor de los cuatro números introducidos y también el menor de ellos.

def bigAndSmall(numList):
    big = numList[0]
    small = numList[0]
    for n in numList[1:]:             
        if n > big:
            big = n
        elif n < small:
            small = n
    return (big, small)

A = 0
B = 0
C = 0
D = 0
numbers = []

while (A == B or A == C or A == D or B == C or B == D or C == D):
    A = input("Introduce a number: ")
    numbers.append(int(A))
    B = input("Introduce other number: ")
    numbers.append(int(B))
    C = input("Introduce another number: ")
    numbers.append(int(C))
    D = input("Introduce the last number: ")
    numbers.append(int(D))
    if (A == B or A == C or A == D or B == C or B == D or C == D):
        numbers = []
        print("The four numbers must be different.")
    
result = bigAndSmall(numbers)
print(result)

class testing(unittest.TestCase):    
    def test01(self):
        self.assertEqual(bigAndSmall([1,2,3,4]), (4,1))

if __name__ == "__main__":
    unittest.main()
