import unittest, math


# Given an array of positive numbers and a positive number ‘k’,
# find the maximum sum of any contiguous subarray of size ‘k’.
def max_sub_array_size_k2(k, arr):
    max_sum = -math.inf

    for i in range(len(arr) - k + 1):
        win_sum = 0
        for j in range(i, i + k):
            win_sum += arr[j]
        max_sum = max(max_sum, win_sum)

    return max_sum

# TC O(N*K)

# a better approach!!!
# subtract the element that goes off the window and add the one that enters

# k = 3, arr = [2, 1, (5, 1, 3), 2]
# len(arr) = 6
# start = 0, 1, 2, 3
# end = 2, 3, 4, 5
# sum_win = 8, 6, 7, 6, 9, 4, 6
# max_sum = 8, 8, 9, 9


def max_sub_array_size_k_me(k, arr):
    start_win, end_win = 0, k - 1
    sum_win = sum(arr[start_win:end_win + 1])
    max_sum = sum_win

    while end_win < len(arr) - 1:
        sum_win -= arr[start_win]
        sum_win += arr[end_win + 1]
        max_sum = max(max_sum, sum_win)
        start_win += 1
        end_win += 1

    return max_sum

# TC O(n), SP O(1)

# site approach:


def max_sub_array_size_k(k, arr):
    start = 0
    max_sum = -math.inf
    win_sum = 0

    for end in range(len(arr)):
        win_sum += arr[end]

        if end >= k - 1:
            max_sum = max(max_sum, win_sum)
            win_sum -= arr[start]
            start += 1

    return max_sum


class TestMaxSumSubarraySizeK(unittest.TestCase):
    def test1(self):
        self.assertEqual(9, max_sub_array_size_k(3, [2, 1, 5, 1, 3, 2]))

    def test2(self):
        self.assertEqual(7, max_sub_array_size_k(2, [2, 3, 4, 1, 5]))


if __name__ == '__main__':
    unittest.main()
