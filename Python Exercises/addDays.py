#sumale días a una fecha y devuelve una tupla en formato día, nombre de mes, año
import unittest
from datetime import date, timedelta

TODAY = date.today()

def addDaysDate(dateFromUser, daysFromUser):
    newDate = dateFromUser + timedelta(days=daysFromUser)
    dayTuple = (newDate.day, newDate.strftime("%B"), newDate.year)
    return dayTuple

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.result = (9, 'July', 2020)

    def test_date(self):
        self.assertEqual(addDaysDate(TODAY, 2), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.result

if __name__ == "__main__":
    unittest.main()