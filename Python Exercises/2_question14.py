import unittest

# Reverse a given integer number

def reverse_number(number):
    number = str(number)
    result = ""
    for n in range(len(number)-1, -1, -1):
        result += number[n]
    return int(result)
    
class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.number = 76542
        self.result = 24567

    def test01(self):
        self.assertEqual(reverse_number(self.number), self.result)
    
    def tearDown(self):
        print("Deleting context...")
        del self.number
        del self.result

if __name__ == "__main__":
    unittest.main()
