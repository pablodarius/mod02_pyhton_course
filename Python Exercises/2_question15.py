import unittest

# Use a loop to display elements from a given list which are present at even positions

def even_positions(numbers):
    result = []
    for i in numbers[1::2]:
        result.append(i)
    return result

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        self.result = [20, 40, 60, 80, 100]

    def test01(self):
        self.assertEqual(even_positions(self.numbers), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.numbers
        del self.result

if __name__ == "__main__":
    unittest.main()
