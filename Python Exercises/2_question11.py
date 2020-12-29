import unittest

# Python program to display all the prime numbers within a range

def is_prime(number):
    for n in range(2, number):
        if number % n == 0:
            return False
    return True

def prime_numbers(start, end):
    for n in range(start, end + 1):
        if is_prime(n):
            print(n)
    
class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.start = 25
        self.end = 50

    def test01(self):
        prime_numbers(self.start, self.end)

    def tearDown(self):
        print("Deleting context...")
        del self.start
        del self.end

if __name__ == "__main__":
    unittest.main()
