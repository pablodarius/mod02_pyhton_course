import unittest

# Given a two list of numbers create a new list such that new list should
# contain only odd numbers from the first list and even numbers from the second list

def join_list(one, two):
    result = []
    for i in one:
        if i % 2 != 0:
            result.append(i)
    
    for i in two:
        if i % 2 == 0:
            result.append(i)

    return result


class testing(unittest.TestCase):
    def setUp(self):
        print("Preparing context...")
        self.numberlist_one = [10, 20, 23, 11, 17]
        self.numberlist_two = [13, 43, 24, 36, 12]
        self.result_list = [23, 11, 17, 24, 36, 12]

    def test01(self):
        self.assertEqual(join_list(self.numberlist_one, self.numberlist_two), self.result_list)

    def tearDown(self):
        print("Deleting context...")
        del self.numberlist_one
        del self.numberlist_two
        del self.result_list


if __name__ == "__main__":
    unittest.main()
