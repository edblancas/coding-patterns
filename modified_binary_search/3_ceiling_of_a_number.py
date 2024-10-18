def find_ceiling_of_a_number(arr, key):
    lo, hi = 0, len(arr) - 1
    if key > arr[-1]: return -1
    while lo <= hi:
        m = (lo + hi) // 2
        if arr[m] == key:
            return m
        elif key > arr[m]:
            lo = m + 1
        else:
            hi = m - 1
    return lo


import unittest

class TestFindCeilingOfANumber(unittest.TestCase):
    def test_find_ceiling_of_a_number(self):
        self.assertEqual(find_ceiling_of_a_number([4, 6, 10], 6), 1)
        self.assertEqual(find_ceiling_of_a_number([1, 3, 8, 10, 15], 12), 4)
        self.assertEqual(find_ceiling_of_a_number([1, 3, 8, 10, 15], 2), 1)
        self.assertEqual(find_ceiling_of_a_number([4, 6, 10], 17), -1)
        self.assertEqual(find_ceiling_of_a_number([4, 6, 10], -1), 0)

def main():
    test = TestFindCeilingOfANumber()
    test.test_find_ceiling_of_a_number()


main()

"""
run bin search and we have:
3 cases for key:
1. equal
    found key, then return it
2. greater <- tricky
    a point where key is greater, immediatly then less than
    so stop and return the last greater
3. there is no = or >
    reach the end of the array and not found
"""
