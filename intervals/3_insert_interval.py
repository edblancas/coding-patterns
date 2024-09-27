# LC 7. Insert Interval
# https://leetcode.com/problems/insert-interval/description/
def insert_interval(
    intervals: list[list[int]], new_interval: list[int]
) -> list[list[int]]:
    # if we omit the key will take more time to sort it
    # as it compares both elements of each interval
    intervals.sort(key=lambda x: x[0])
    res = []
    i = 0
    length = len(intervals)

    # asume the new_interval is > than the first interval
    while i < length and intervals[i][1] < new_interval[0]:
        res.append(intervals[i])
        i += 1

    # check if new interval overlaps then merge
    while i < length and new_interval[1] >= intervals[i][0]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    res.append(new_interval)

    while i < length:
        res.append(intervals[i])
        i += 1

    return res


import unittest

class TestInsertInterval(unittest.TestCase):
    def test_insert_interval(self):
        self.assertEqual(insert_interval([[1,3], [5,7], [8,12]], [4,6]), [[1,3], [4,7], [8,12]])

if __name__ == '__main__':
    unittest.main()

