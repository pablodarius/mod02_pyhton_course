import unittest

# Display a message “Done” after successful execution of for loop

def print_minus_number(bottom):
    for i in range(bottom, 0, 1):
        print(i)
    else:
        print("Done!")
    
class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.number = -10

    def test01(self):
        print_minus_number(self.number)

    def tearDown(self):
        print("Deleting context...")
        del self.number

if __name__ == "__main__":
    unittest.main()
