import unittest

# Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def do_pattern(number):
    for i in range(1, number+1):
        for j in range(1, i+1):
            print(i, end=" ")
        print("\n")
        

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.number = 5

    def test01(self):
        do_pattern(self.number)

    def tearDown(self):
        print("Deleting context...")
        del self.number

if __name__ == "__main__":
    unittest.main()
