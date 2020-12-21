import unittest

# Print multiplication table form 1 to 10

def multi_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i*j, end=" ")
        print("\b")

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")

    def test01(self):
        multi_table()

    def tearDown(self):
        print("Deleting context...")
 
if __name__ == "__main__":
    unittest.main()
