# O(n log n) time, O(1) space
def find_missing_number_me(nums):
    nums.sort()
    for i, n in enumerate(nums):
        if n != i:
            return i

def find_missing_number(nums):
    n = len(nums)
    i = 0
    while i < n:
        j = nums[i]
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            continue
        i += 1

    for i, num in enumerate(nums):
        if num != i:
            return i

    return n


import unittest


class TestMissing(unittest.TestCase):
    def test_missing(self):
        self.assertEqual(find_missing_number([4, 0, 3, 1]), 2)


if __name__ == "__main__":
    unittest.main()
