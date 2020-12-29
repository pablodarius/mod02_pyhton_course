import unittest

# Print the following pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

def asterisk_sequence(number):
    for n in range(number):
        for i in range(n):
            print("*", end=" ")
        print("\b")

    for n in range(number, 0, -1):
        for i in range(n):
            print("*", end=" ")
        print("\b")

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.number = 5

    def test01(self):
        asterisk_sequence(self.number)

    def tearDown(self):
        print("Deleting context...")
        del self.number

if __name__ == "__main__":
    unittest.main()
