import unittest

def toTen(top):
    number_list = []
    for t in range(1, 11, 1):
        number_list.append(t)

    return number_list


class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.numbersList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.top = 10

    def test01(self):
        print("test01...")
        self.assertEqual(toTen(self.top), self.numbersList)
    
    def tearDown(self):
        print("Deleting context...")
        del self.numbersList
        del self.top

if __name__ == "__main__":
    unittest.main()