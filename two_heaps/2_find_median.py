"""
1-based-index
The median is the middle value in a set of data. First, organize and order the data from 
smallest to largest. Divide the number of observations by two to find the midpoint value. 
Round the number up if there's an odd number of observations and the value in that 
position is the median.
Take the average of the values found above and below that position if the number of 
observations is even.

Med(X)
= x[(n+1)/2], if n is odd
= (x[n/2] + x[n/2 + 1]) /2), if n is even
X	=	ordered list of values in data set
n	=	number of values in data set
"""

from heapq import heappush, heappop

smallNums = []
largerNums = []


def insertNum(num):
    if not smallNums or num <= -smallNums[0]:
        heappush(smallNums, -num)
    else:
        heappush(largerNums, num)

    if len(smallNums) - len(largerNums) >= 2:
        heappush(largerNums, -heappop(smallNums))
    elif len(largerNums) - len(smallNums) >= 1:
        heappush(smallNums, -heappop(largerNums))


def findMedian():
    length = len(smallNums) + len(largerNums)
    if length % 2 == 1:
        return -smallNums[0]
    return (-smallNums[0] + largerNums[0]) / 2


import unittest


class TestMedian(unittest.TestCase):
    def test_median(self):
        insertNum(3)
        insertNum(1)
        self.assertEqual(findMedian(), 2.0)
        insertNum(5)
        self.assertEqual(findMedian(), 3.0)
        insertNum(4)
        self.assertEqual(findMedian(), 3.5)


def main():
    test = TestMedian()
    test.test_median()


main()

"""
smallNums gonna have 1 more, in case of even

maxHeap smallNums = h[-1,-3]
minHeap largeNums = h[5]
"""

