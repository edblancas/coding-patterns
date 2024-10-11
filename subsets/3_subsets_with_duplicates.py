def find_subsets(nums):
    nums.sort()
    res = [[]]
    for i in range(len(nums)):
        if i >= 1 and nums[i] == nums[i-1]:
            j = len(res) - j - 1
        else:
            j = 0
        for j in range(j, len(res)):
            sub = list(res[j])
            sub.append(nums[i])
            res.append(sub)
    return res


import unittest

class TestFindSubsets(unittest.TestCase):
    def test_find_subsets(self):
        nums = [1,3,3]
        self.assertEqual(find_subsets(nums), [[], [1], [3], [1,3], [3,3], [1,3,3]])

def main():
    test = TestFindSubsets()
    test.test_find_subsets()
    print('done!')

main()
