# Given an array of positive numbers and a positive number ‘S’, find the length
# of the smallest contiguous subarray whose sum is greater than or equal to ‘S’.
# Return 0, if no such subarray exists.
#
# Example 1:
#
# Input: [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
# Example 2:
#
# Input: [2, 1, 5, 2, 8], S=7
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
# Example 3:
#
# Input: [3, 4, 1, 1, 6], S=8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
import math
import unittest


# start, end = 0, 0
# smallest_win_len = math.inf
# sum = arr[start]
# edge case if sum >= S then return 1
#
# while start < len(arr) and end < len(arr):
#   if sum >= S:
#       smallest_win_len = min(end - start + 1, smallest_win_len)
#       while True:
#           sum -= arr[start]
#           start += 1
#           if sum < S or start >= len(arr):
#               break
#   else:
#       while True:
#           end += 1
#           sum += arr[end]
#           if sum >= S or end >= len(arr):
#               break
#
# return smallest_win_len
#
# THE ABOVE CODE THROWS OUT OF BOUND EXCEPTION


def smallest_subarray_with_given_sum(s, arr):
    sum_win = 0
    start = 0
    smallest_win = math.inf

    for end in range(len(arr)):
        sum_win += arr[end]
        
        while sum_win >= s:
            smallest_win = min(smallest_win, end - start + 1)
            sum_win -= arr[start]
            start += 1

    return smallest_win if smallest_win != math.inf else 0

# TC O(N)
# The outer for loop runs for all elements and the inner while loop processes
# each element only once, therefore the time complexity of the algorithm will be
# O(N+N) which is asymptotically equivalent to O(N).

# SC O(1)


class Test(unittest.TestCase):
    def test_smallest_subarray_with_given_sum(self):
        self.assertEqual(2, smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))

    def test_smallest_subarray_with_given_sum_2(self):
        self.assertEqual(1, smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))

    def test_smallest_subarray_with_given_sum_3(self):
        self.assertEqual(3, smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]))
