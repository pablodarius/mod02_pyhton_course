import unittest

# Calculate income tax for the given income by adhering to the below rules
# Taxable Income	Rate (%)
# First $10,000	0
# Next $10,000	10
# The remaining	20

def taxing(income):
    taxPayable = 0
    if income > 10000:
        income -= 10000
        if income > 10000:
            income -= 10000
            taxPayable += 10000 * 0.1

    taxPayable += income * 0.2
    return taxPayable


class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.income = 45000
        self.taxPayable = 6000

    def test01(self):
        self.assertEqual(taxing(self.income), self.taxPayable)

    def tearDown(self):
        print("Deleting context...")
        del self.income
        del self.taxPayable

if __name__ == "__main__":
    unittest.main()
