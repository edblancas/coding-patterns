def binary_search(arr, key):
    isAsc = arr[0] > arr[-1]

    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        m = (lo + hi) // 2
        if arr[m] == key:
            return m
        elif key > arr[m]:
            if not isAsc:
                hi = m - 1
            else:
                lo = m + 1
        else:
            if not isAsc:
                lo = m + 1
            else:
                hi = m - 1

    return -1


import unittest

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        self.assertEqual(binary_search([4, 6, 10], 10), 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7], 5), 4)
        self.assertEqual(binary_search([10, 6, 4], 10), 0)
        self.assertEqual(binary_search([10, 6, 4], 4), 2)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7], 99), -1)

def main():
    test = TestBinarySearch()
    test.test_binary_search()


main()
