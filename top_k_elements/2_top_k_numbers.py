from heapq import heappop, heappush

def find_k_largest_numbers(nums, k):
    result = []
    for n in range(0, k):
        heappush(result, nums[n])

    for n in range(3, len(nums)):
        if nums[n] > result[0]:
            heappop(result)
            heappush(result, nums[n])

    return result

"""
complexity
time: O(k log n + (n - k) log n) = O(n log k)
space: O(k)
"""


import unittest

class TestFindKLargestNumbers(unittest.TestCase):
    def test_find_k_largest_numbers(self):
        self.assertEqual(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3), [5, 12, 11])
        self.assertEqual(find_k_largest_numbers([5, 12, 11, -1, 12], 3), [11, 12, 12])

def main():
    test = TestFindKLargestNumbers()
    test.test_find_k_largest_numbers()


main()
