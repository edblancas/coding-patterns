from dataclasses import dataclass
from heapq import heappush, heappop

@dataclass
class Point:
    x: int
    y: int

def find_closes_points(points, k):
    heap = []
    def euc(p): return pow(p.x, 2) + pow(p.y, 2)
    for i in range(k):
        heappush(heap, (-euc(points[i]), points[i]))

    print('-->', heap)

    for i in range(k, len(points)):
        print(euc(points[i]), -heap[0][0])
        if euc(points[i]) < -heap[0][0]:
            heappop(heap)
            heappush(heap, (-euc(points[i]), points[i]))

    return [item[1] for item in heap]

"""
heap [(-5, P(1,2))]
(10, P(1,3))

complexity
time O(k log k + (n - k) log k) = O(n log k)
space O(k)
"""


import unittest

class TestFindClosesPoints(unittest.TestCase):
    def test_find_closes_points(self):
        self.assertEqual(find_closes_points([Point(1,2),Point(1,3)], 1), 
                         [Point(1,2)])
        self.assertEqual(find_closes_points([Point(1,3),Point(3,4),Point(2,-1)], 2), 
                         [Point(1,3), Point(2,-1)])

def main():
    test = TestFindClosesPoints()
    test.test_find_closes_points()


main()
