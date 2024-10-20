from heapq import heappush, heappop, heapify

def minimum_cost_to_connect_ropes(rope_lengthts):
    heapify(rope_lengthts)
    res = 0
    while len(rope_lengthts) > 1:
        new = heappop(rope_lengthts) + heappop(rope_lengthts)
        heappush(rope_lengthts, new)
        res += new
        print(rope_lengthts,res)
    return res

"""
r=0
[1,3,5,11]

r=4
[4,5,11]

r=13
[9,11]

r=33
[20]

complexity
time O(n) + O(n log n)
space O(n)
"""


import unittest

class TestMinimumCostToConnectRoper(unittest.TestCase):
    def test_minimum_cost_to_connect_roper(self):
        self.assertEqual(minimum_cost_to_connect_ropes([1, 3, 11, 5]), 33)
        self.assertEqual(minimum_cost_to_connect_ropes([3, 4, 5, 6]), 36)
        self.assertEqual(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2]), 42)

def main():
    test = TestMinimumCostToConnectRoper()
    test.test_minimum_cost_to_connect_roper()


main()
