from heapq import heappop, heappush
from collections import defaultdict

def find_k_frequent_numbers(nums, k):
    hm = defaultdict(int)
    for n in nums:
        hm[n] += 1

    heap = []
    keys = list(hm.keys())
    for i in range(k):
        key = keys[i]
        heappush(heap, (hm[key], key))
        
    for i in range(k, len(keys)):
        key = keys[i]
        if hm[key] > heap[0][0]:
            heappop(heap)
            heappush(heap, (hm[key], key))

    return [freq[1] for freq in heap]


"""
[1, 3, 5, 12, 11, 12, 11], K = 2
{1:1, 3:1, 5:1, 12:2, 11:2}
[1,3,5,12,11]
min heap
[(2,12), (2,11)]

complexity:
time O(n + k log k + (n-k) log k) = O(n log k)
space O(n)
"""


import unittest

class TestFindKFrequentNumbers(unittest.TestCase):
    def test_find_k_frequent_numbers(self):
        res = find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)
        self.assertEqual(set(res), {11, 12})
        res = find_k_frequent_numbers([5, 12, 11, 3, 11], 2)
        print('res', res)
        self.assertTrue(tuple(res) in {(11,5), (5,11), (11,12), (12,11), (11,3), (3,11)})

def main():
    test = TestFindKFrequentNumbers()
    test.test_find_k_frequent_numbers()


main()
