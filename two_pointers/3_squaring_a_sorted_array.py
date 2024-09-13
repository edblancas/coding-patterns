# easy
# Given a sorted array, create a new array containing squares of all the number
# of the input array in the sorted order.

def make_squares(arr):
    lo = 0
    hi = len(arr) - 1
    res = [0] * len(arr)
    pt = hi
    while lo <= hi:
        sq1 = arr[lo] * arr[lo]
        sq2 = arr[hi] * arr[hi]
        if sq1 > sq2:
            res[pt] = sq1
            lo += 1
        else:
            res[pt] = sq2
            hi -= 1
        pt -= 1
    return res

import unittest

class TestMakeSquares(unittest.TestCase):
    def test_make_squares(self):
        self.assertEqual(make_squares([-2, -1, 0, 2, 3]), [0, 1, 4, 4, 9])
        self.assertEqual(make_squares([-3, -1, 0, 1, 2]), [0, 1, 1, 4, 9])

if __name__ == '__main__':
    unittest.main()
