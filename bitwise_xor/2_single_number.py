def find_single_number_1(arr):
    res = arr[0]
    for i in range(1, len(arr)):
        res ^= arr[i]

    return res

# we can use 0 as initial value
# as 0 ^ any number = number
def find_single_number(arr):
    res = 0
    for n in arr:
        res ^= n

    return res


import unittest

class TestFindSingleNumber(unittest.TestCase):
    def test_find_single_number(self):
        self.assertEqual(find_single_number([1, 4, 2, 1, 3, 2, 3]), 4)
        self.assertEqual(find_single_number([7, 9, 7]), 9)

def main():
    test = TestFindSingleNumber()
    test.test_find_single_number()


main()
