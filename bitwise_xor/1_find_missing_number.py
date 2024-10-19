# Commutative and Associative, and distributive laws
# https://www.mathsisfun.com/associative-commutative-distributive.html
def find_missing_number_xor(arr):
    res = 1
    for n in range(2, len(arr)+2):
        res ^= n

    for n in arr:
        res ^= n

    return res


def find_missing_number(arr):
    return find_missing_number_xor(arr)


import unittest

class TestFindMissingNumber(unittest.TestCase):
    def test_find_missing_number(self):
        self.assertEqual(find_missing_number([1, 5, 2, 6, 4]), 3)

def main():
    test = TestFindMissingNumber()
    test.test_find_missing_number()


main()
