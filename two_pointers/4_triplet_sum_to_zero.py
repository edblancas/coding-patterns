# medium
# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

def search_triplets(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if i > 0 and arr[i - 1] == arr[i]:
            continue
        search_pair(arr, -arr[i], i+1, triplets)
    return triplets

def search_pair(arr, target_sum, lo, triplets):
    hi = len(arr) - 1
    while lo < hi:
        curr_sum = arr[lo] + arr[hi]
        if curr_sum == target_sum:
            triplets.append([-target_sum, arr[lo], arr[hi]])
            lo += 1
            hi -= 1
            while lo < hi and arr[lo-1] == arr[lo]:
                lo += 1
            while lo < hi and arr[hi+1] == arr[hi]:
                hi -= 1
        elif curr_sum < target_sum:
            lo += 1
        else:
            hi -= 1

"""
Time complexity
Sorting the array will take O(n log n) time complexity.
The search_pair fn will take O(n) time, and we do this for every number in the
    input array, so O(n^2).
This means search_triplets will take O(n log n + n^2) time, wich is
    asymptotically equivalent to O(n^)

Space complexity
Ignoring the space required for the output array, the space complexity
    of the above algorithm will be o(n) wich is required for sorting.
Py uses timsort that is O(n log n) time and O(n) space.
"""

class Solution:
    def threeSum(self, nums):
        nums.sort()
        triplets = []
        def find_pair():
            nonlocal triplets
            target = -nums[i - 1]
            lo = i
            hi = len(nums) - 1
            while lo < hi:
                curr_sum = nums[lo] + nums[hi]
                if curr_sum == target:
                    triplets.append([-target, nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif curr_sum < target:
                    lo += 1
                else:
                    hi -= 1

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            find_pair()
        return triplets
# [-1,0,1,2,-1,-4]
# this sol not work cuz we are skipping one -1,
# cuz we are comparing ahead of the current,
# the statement says the indices of the used numbers are distinct,
# but noting that use number value repeated
# [-4,-1,-1,0,1,2]
# the result would be [[-1,0,1]]
# and the corret one is [[-1,-1,2],[-1,0,1]]

import unittest

class TestSearchTriplets(unittest.TestCase):
    def test_search_triplets(self):
        self.assertEqual(search_triplets([-3, 0, 1, 2, -1, 1, -2]), [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]])
        self.assertEqual(search_triplets([-5, 2, -1, -2, 3]), [[-5, 2, 3], [-2, -1, 3]])

if __name__ == '__main__':
    unittest.main()
