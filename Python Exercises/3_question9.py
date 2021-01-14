import unittest

# Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters

def sum_and_average(input_str):
    nums = []
    aux_nums = []
    for s in input_str:
        if s.isdigit():
            aux_nums.append(s)
        else:
            if aux_nums:
                num = "".join(aux_nums)
                nums.append(int(num))
                aux_nums = []
    if aux_nums:
        num = "".join(aux_nums)
        nums.append(int(num))

    elements_sum = sum(nums)
    return [elements_sum, (elements_sum / len(nums))]

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
