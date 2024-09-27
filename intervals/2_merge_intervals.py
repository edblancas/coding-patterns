"""
Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
"""

def merge(intervals):
    intervals.sort()
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(interval[1], merged[-1][1])

    return merged


import unittest

class TestMergeIntervals(unittest.TestCase):
    def test_merge_intervals(self):
        self.assertEqual(merge([[1,4], [2,5], [7,9]]), [[1,5],[7,9]])
        self.assertEqual(merge([[6,7], [2,4], [5,9]]), [[2,4], [5,9]])
        self.assertEqual(merge([[1,4], [2,6], [3,5]]), [[1,6]])
        self.assertEqual(merge([[1,4], [2,6], [3,5], [8,9], [11,13], [12,15]]),
                         [[1,6], [8,9], [11,15]])

if __name__ == '__main__':
    unittest.main()
