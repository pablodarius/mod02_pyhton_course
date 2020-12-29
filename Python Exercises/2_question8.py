import unittest

# Invierta la siguiente lista usando el bucle for

def reverse_list(numbers):
    result = []
    for n in range(len(numbers)-1, -1, -1):
        result.append(numbers[n])
    return result
    
class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.numbers = [10, 20, 30, 40, 50]
        self.result = [50, 40, 30, 20, 10]

    def test01(self):
        self.assertEqual(reverse_list(self.numbers), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.numbers
        del self.result


if __name__ == "__main__":
    unittest.main()
