# easy
# Given an array of sorted numbers, remove all duplicates from it.
# You should not use any extra space; after removing the duplicates
# in-place return the new length of the array.

def remove_duplicates(arr):
    next_non_dup = 1
    next = 1
    while next < len(arr):
        # arr[next_non_dup - 1] is the last no duplicated num *,
        # ie [1*,2^,2,3] the first iteration ^ is next
        # ie [1,2*,2^,3] the second iteration
        if arr[next_non_dup - 1] != arr[next]:
            arr[next_non_dup] = arr[next]
            next_non_dup += 1
        next += 1
    return next_non_dup

import unittest

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        # The first four elements after removing the duplicates will be [2, 3, 6, 9].
        self.assertEqual(remove_duplicates([2, 3, 3, 3, 6, 9, 9]), 4)
        # The first two elements after removing the duplicates will be [2, 11].
        self.assertEqual(remove_duplicates([2, 2, 2, 11]), 2)

if __name__ == '__main__':
    unittest.main()

