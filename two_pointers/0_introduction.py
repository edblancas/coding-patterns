# easy
# get the pair of elements that sum the target t in a sorted array arr

def target_sum(arr, t):
    lo = 0
    hi = len(arr) - 1
    while lo < hi:
        sum = arr[lo] + arr[hi]
        if sum == t:
            return True
        elif sum < t:
            lo += 1
        else:
            hi -= 1
    return False

import unittest

class TestTargetSum(unittest.TestCase):
    def test_target_sum(self):
        self.assertEqual(target_sum([1,2,3,4,6], 6), True)

if __name__ == '__main__':
    unittest.main()
