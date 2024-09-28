"""
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.
"""

import collections

Interval = collections.namedtuple("Interval", ["start", "end"])


def intersection(intervals1, intervals2):
    i, j = 0, 0
    res = []
    # while i and j are in the range of the intervals do:
    while i < len(intervals1) and j < len(intervals2):
        # check it intervals1[i] overlaps intervals2[j], or viceversa
        a_overlaps_b = (
            intervals1[i].start <= intervals2[j].end
            and intervals1[i].end > intervals2[j].start
        )
        b_overlaps_a = (
            intervals2[j].start <= intervals1[i].end
            and intervals2[j].end > intervals1[i].start
        )

        # if there are overlap then we get the intersection of the two intervals
        if a_overlaps_b or b_overlaps_a:
            res.append(
                Interval(
                    max(intervals1[i].start, intervals2[j].start),
                    min(intervals1[i].end, intervals2[j].end),
                )
            )

        # we advance the pointer of the intervals that finish first
        # i.e. the one that ends first will already be included in the
        # intersection calculated before
        # we don't need to check again the instersectio calculated cuz the lists
        # have disjoint intervals
        # from chatgpt
        #  Once an interval ends, it cannot possibly overlap with any future 
        #  intervals because they are sorted. Therefore, the interval that finishes first 
        #  (i.e., has the smaller end time) cannot overlap with any of the remaining 
        #  intervals from the other list, so we can safely move its pointer forward.
        #  e.g.
        #  intervals1 = [[1, 3], [5, 6], [7, 9]]
        #  intervals2 = [[2, 5], [7, 10]]
        #  [1,3] and [2,5]
        #  the 1,3 cannot overlap with the next 7,10 of the other list
        #  cuz they are sorted and disjointed
        if intervals1[i].end < intervals2[j].end:
            i += 1
        else:
            j += 1

        # also if one list terminates first, then we are sure that the last
        # interval of the other list will not overlap with the remaining
        # so we don't do anything

    return res


import unittest


class TestIntersect(unittest.TestCase):
    def test_intersect(self):
        self.assertEqual(
            intersection(
                [Interval(1, 3), Interval(5, 6), Interval(7, 9)],
                [Interval(2, 3), Interval(5, 7)],
            ),
            [Interval(2, 3), Interval(5, 6), Interval(7, 7)],
        )


if __name__ == "__main__":
    unittest.main()
