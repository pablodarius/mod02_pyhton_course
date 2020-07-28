import unittest

# Desarrolle un algoritmo que funcione como caja registradora, recibir productos (codigo y precio) y emitir precio total con iva 21%

def linearSearching(numbers, num):
    i = 0
    for n in numbers:
        if num == n:
            return i
        i += 1
    return -1

def binarySearch(numbers, num):
    left = 0
    right = len(numbers) - 1

    while  left <= right:
        mid = round((left + right) / 2)
        print(F"left: {left}, right: {right}, middle: {mid}")

        if numbers[mid] == num:
            return mid
        elif numbers[mid] > num:
            right = mid - 1
        else:
            left = mid + 1

    return -1

def recursiveBinarySearch(numbers, num, left, right):
    if left > right: 
        return -1

    while  left <= right:
        mid = round((left + right) / 2)
        print(F"left: {left}, right: {right}, middle: {mid}")

        if numbers[mid] == num:
            return mid
        elif numbers[mid] > num:
            right = mid - 1
        else:
            left = mid + 1

    return recursiveBinarySearch(numbers, num, left, right)


class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.numbersList = (1, 2, 3, 4, 5, 6, 10)
        self.num = 6
        self.notNum = 9

    def test01_lineal(self):
        print("test01_lineal...")
        self.assertEqual(linearSearching(self.numbersList, self.num), 5)
    def test02_lineal(self):
        print("test02_lineal...")
        self.assertEqual(linearSearching(self.numbersList, self.notNum), -1)
    def test01_binary(self):
        print("test01_binary...")
        self.assertEqual(binarySearch(self.numbersList, self.num), 5)
    def test02_binary(self):
        print("test02_binary...")
        self.assertEqual(binarySearch(self.numbersList, self.notNum), -1)
    def test01_recursiveBinary(self):
        print("test01_recursiveBinary...")
        self.assertEqual(recursiveBinarySearch(self.numbersList, self.num, 0, len(self.numbersList) - 1), 5)
    def test02_recursiveBinary(self):
        print("test02_recursiveBinary...")
        self.assertEqual(recursiveBinarySearch(self.numbersList, self.notNum, 0, len(self.numbersList) - 1), -1)
    def tearDown(self):
        print("Deleting context...")
        del self.num
        del self.notNum

if __name__ == "__main__":
    unittest.main()