def find_subsets(nums):
    res = [[]]
    for n in nums:
        for i in range(len(res)):
            sub = list(res[i])
            sub.append(n)
            res.append(sub)
    return res

"""
[1,5,3]
res = [[], [1,]]
n = 2
sub = [[]]
s = [1]
"""

import unittest

class TestFindSubsets(unittest.TestCase):
    def test_find_subsets(self):
        nums = [1,5,3]
        self.assertEqual(find_subsets(nums), [[], [1], [5], [1,5], [3], [1,3], [5,3], [1,5,3]])

def main():
    test = TestFindSubsets()
    test.test_find_subsets()

main()
