import unittest

# Acepte el número del usuario y calcule la suma de todos los números entre 1 y el número dado

def summatory(top):
    try: 
        int(top)
        result = top
        for i in range(1, top):
            result += (top - i)
        return result
    except:
        return False

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.top = 10
        self.wrong_top = "ten"
        self.result = 55

    def test01_ok(self):
        self.assertEqual(summatory(self.top), self.result)
    
    def test02_wrong(self):
        self.assertFalse(summatory(self.wrong_top))

    def tearDown(self):
        print("Deleting context...")
        del self.top
        del self.wrong_top
        del self.result


if __name__ == "__main__":
    unittest.main()
