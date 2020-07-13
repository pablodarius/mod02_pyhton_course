#sumale días a una fecha y devuelve una tupla en formato día, nombre de mes, año
import unittest

def countLetters(sentence, numLetters):
    counter = 0
    sentenceList = sentence.split()
    for s in sentenceList:
        if len(s) == numLetters:
            counter += 1

    return counter

def autoTelegram(sentence, costShort, costLong, longMax):
    totalCost = 0
    result = ""
    sentenceList = sentence.split()

    for s in sentenceList:
        if "." in s:
            s.replace(".", "")
            pointAux = "STOP "
        else:
            pointAux = ""

        if len(s) > longMax:
            result += s[:longMax] + "@ "
            totalCost += costShort
        else:
            result += s + " "
            totalCost += costLong
        result += pointAux   

    result += "STOPSTOP"
    print(F"Telgram Total Price: {totalCost} ")
    return result

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.intro1 = "Look at that asshole"
        self.intro2 = "The rain in Spain stays mainly in the plain"
        self.intro3 = " Llego mañana alrededor del mediodía. Voy a almorzar "
        self.intro3_result = "Llego mañan@ alred@ del medio@ STOP Voy a almor@ STOPSTOP"
        self.costShort = 1
        self.costLong = 2

    def test_count_01(self):
        self.assertEqual(countLetters(self.intro1, 4), 2)

    def test_count_02(self):
        self.assertEqual(countLetters(self.intro2, 5), 3)

    def test_telegram(self):
        self.assertEqual(autoTelegram(self.intro3, self.costShort, self.costLong, 5), self.intro3_result)

    def tearDown(self):
        print("Deleting context...")
        del self.intro1
        del self.intro2
        del self.intro3
        del self.intro3_result
        del self.costShort
        del self.costLong

if __name__ == "__main__":
    unittest.main()