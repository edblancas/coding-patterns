# MEDIUM

# Given an array of characters where each character represents a fruit tree,
# you are given two baskets and your goal is to put maximum number of fruits in
# each basket. The only restriction is that each basket can have only one type of fruit.
#
# You can start with any tree, but once you have started you can’t skip a tree.
# You will pick one fruit from each tree until you cannot, i.e., you will stop
# when you have to pick from a third fruit type.
#
# Write a function to return the maximum number of fruits in both the baskets.
#
# Example 1:
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the
# subarray ['C', 'A', 'C']
#
# Example 2:
# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
import unittest


def fruits_into_baskets(fruits):
    max_fruits = 0
    start = 0
    baskets = {}

    for end in range(len(fruits)):
        baskets[fruits[end]] = baskets.get(fruits[end], 0) + 1

        while len(baskets) > 2:
            baskets[fruits[start]] -= 1
            if baskets[fruits[start]] == 0:
                del baskets[fruits[start]]
            start += 1

        # this is the same as end - start + 1
        # curr_count = 0
        # for count in baskets.values():
        #     curr_count += count

        max_fruits = max(max_fruits, end - start + 1)

    return max_fruits


class Test(unittest.TestCase):
    def test_fruits_into_baskets(self):
        self.assertEqual(3, fruits_into_baskets(['A', 'B', 'C', 'A', 'C']))

    def test_fruits_into_baskets_2(self):
        self.assertEqual(5, fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
