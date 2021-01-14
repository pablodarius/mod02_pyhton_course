import unittest
import re

# Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters

def sum_and_average(str):
    markList = [int(num) for num in re.findall(r'\b\d+\b', str)]
    totalMarks = 0
    for mark in markList:
        totalMarks+=mark
    percentage = totalMarks/len(markList)
    return [totalMarks, percentage]

class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.str = "English = 78 Science = 83 Math = 68 History = 65"
        self.result = [294, 73.5]

    def test01(self):
        self.assertEqual(sum_and_average(self.str), self.result)

    def tearDown(self):
        print("Deleting context...")
        del self.str
        del self.result

if __name__ == "__main__":
    unittest.main()
