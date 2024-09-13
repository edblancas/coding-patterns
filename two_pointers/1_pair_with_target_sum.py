# Given an array of sorted numbers and a target sum, find a 
# pair in the array whose sum is equal to the given target.

def pair_with_target_sum(arr, target_sum):
    curr_sum = 0
    lo = 0
    hi = len(arr) - 1
    while lo < hi:
        curr_sum = arr[lo] + arr[hi]
        if curr_sum == target_sum:
            return [lo, hi]
        elif curr_sum < target_sum:
            lo += 1
        else:
            hi -= 1
    return []

import unittest

class TestPairWithTargetSum(unittest.TestCase):
    def test_pair_with_target_sum(self):
        self.assertEqual(pair_with_target_sum([1, 2, 3, 4, 6], 6), [1, 3])
        self.assertEqual(pair_with_target_sum([2, 5, 9, 11], 11), [0, 2])

if __name__ == '__main__':
    unittest.main()
