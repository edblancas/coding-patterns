def find_averages_of_subarrays(K, arr):
    sum_subarr = 0
    res = []
    start_window = 0
    for end_window in range(len(arr)):
        # add the next element
        sum_subarr += arr[end_window]
        # slide the window, we dont need to slide it if we've not hit the
        # required window of size K
        if end_window >= K - 1:
            res.append(sum_subarr/K)  # calculate the avg
            sum_subarr -= arr[start_window]  # substrac the element going out
            start_window += 1  # slide the window ahead
    return res

import unittest
class TestFindAveragesOfSubarrays(unittest.TestCase):
    def test_1(self):
        self.assertEqual(find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]), [2.2, 2.8, 2.4, 3.6, 2.8])

if __name__ == '__main__':
    unittest.main()
