from collections import deque
def find_permutation(nums):
    old_permutations = deque([[]])
    res = []
    for n in nums:
        # this is a pattern used in other places with a queue
        for _ in range(len(old_permutations)):
            new_perm = old_permutations.popleft()
            for place in range(len(new_perm)+1):
                num_perm = list(new_perm)
                num_perm.insert(place, n)
                if len(num_perm) == 3:
                    res.append(num_perm)
                else:
                    old_permutations.append(num_perm)
                print(num_perm)

    print(res)
    return res


import unittest

class TestFindPermutation(unittest.TestCase):
    def test_find_permutation(self):
        nums = [1,2,3]
        self.assertEqual(find_permutation(nums), [[3,2,1], [2,3,1], [2,1,3], [3,1,2], [1,3,2], [1,2,3]])

def main():
    test = TestFindPermutation()
    test.test_find_permutation()


main()

"""
[1,2,3]
res=[[],[1],[2], [2,1], [1,2]]
elem3=[]
n=1,2
sub=[1]
place=0
new=[2,1]




[]
[] [1]
[] [1] [2] [2,1] [1,2]
[] [1] [2] [2,1] [1,2] [3] [1,3] .... [3,2,1] [2,3,1] [2,1,3] [3,1,2] [1,3,2] [1,2,3]
"""
