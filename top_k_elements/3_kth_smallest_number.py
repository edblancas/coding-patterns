"""
[3,4,2,5]
[2,3,4,5]
   2kth
max heap of the smallest numbers
k = 2
heap[0] is the kth smalles number in the arr
[4,3]
[3*,2]
"""

from heapq import heappush, heappop

def find_kth_smallest_number(nums, k):
    if len(nums) < k: return -1

    heap = []
    for i in range(0, k):
        heappush(heap, -nums[i])

    for i in range(k, len(nums)):
        if nums[i] < -heap[0]:
            heappop(heap)
            heappush(heap, -nums[i])

    return -heap[0]

import unittest

class TestFindKthSmallestNumber(unittest.TestCase):
    def test_find_kth_smallest_number(self):
        self.assertEqual(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 3), 5)
        self.assertEqual(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 4), 5)
        self.assertEqual(find_kth_smallest_number([5, 12, 11, -1, 12], 3), 11)

def main():
    test = TestFindKthSmallestNumber()
    test.test_find_kth_smallest_number()


main()
