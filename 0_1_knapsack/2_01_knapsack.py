def knapsack(profits, weights, capacity):
    # the capacity + 1 is to not doint -1 in the memo write and read
    memo = [[None] * len(profits) for _ in range(capacity+1)]
    print(memo)
    return knapsack_memo(profits, weights, capacity, 0, memo)

def knapsack_rec(profits, weights, capacity, curr_item):
    if capacity <= 0 or curr_item >= len(profits):
        return 0

    with_item = 0
    # without this we will caount the profit of the curr_item even if it excceds
    # the capacity
    if weights[curr_item] <= capacity:
        with_item = profits[curr_item] + knapsack_rec(profits, 
                                                      weights, 
                                                      capacity - weights[curr_item], 
                                                      curr_item + 1)
    without_item = knapsack_rec(profits, weights, capacity, curr_item + 1)

    return max(with_item, without_item)


def knapsack_memo(profits, weights, capacity, curr_item, memo):
    if capacity <= 0 or curr_item >= len(profits):
        return 0
    print(capacity, curr_item)
    if memo[capacity][curr_item]:
        print(capacity, curr_item)
        return memo[capacity][curr_item]

    with_item = 0
    if weights[curr_item] <= capacity:
        with_item = profits[curr_item] + knapsack_memo(profits,
                                                       weights,
                                                       capacity - weights[curr_item],
                                                       curr_item + 1,
                                                       memo)
    without_item = knapsack_memo(profits, weights, capacity, curr_item + 1, memo)

    print(capacity, curr_item)
    memo[capacity][curr_item] = max(with_item, without_item)
    return memo[capacity][curr_item]


def knapsack_bottom_up(profits, weights, capacity):
    dp = [[0]*(capacity+1) for _row in range(len(profits))]

    for curr_capacity in range(capacity+1):
        if weights[0] <= curr_capacity:
            dp[0][curr_capacity] = profits[0]

    for item in range(len(profits)):
        for curr_capacity in range(capacity+1):
            include_i = (profits[item] + dp[item - 1][curr_capacity - weights[item]] 
                         if curr_capacity - weights[item] >= 0 
                         else 0)
            not_include_i = dp[item - 1][curr_capacity]
            dp[item][curr_capacity] = max(include_i, not_include_i)

    print(dp)

    return dp[-1][-1]


# as we only need the last row we can use a dp table with just 2 rows
# with %2 we alternate, so:
#   1st row the prev row will be the 0
#   2nd row the actual will be 0 and the prev row will be the 1 (filled in the
#     above step)
#   3rd row actual index will be 1 and prev row index 0
#   And, so on...
def knapsack_bottom_up_2row(profits, weights, capacity):
    dp = [[0]*(capacity + 1) for _ in range(2)]
    for curr_capacity in range(capacity + 1):
        if weights[0] <= curr_capacity:
            dp[0][curr_capacity] = profits[0]

    for curr_item in range(len(profits)):
        for curr_capacity in range(capacity + 1):
            include_curr_item = 0
            not_include_curr_item = 0
            if weights[curr_item] <= curr_capacity:
                include_curr_item = profits[curr_item] + dp[(curr_item-1)%2][curr_capacity - weights[curr_item]] 
        
            not_include_curr_item = dp[(curr_item-1)%2][curr_capacity]
        
            dp[curr_item%2][curr_capacity] = max(include_curr_item, not_include_curr_item)

    return dp[-1][-1]


def knapsack_bottom_up_1row(profits, weights, capacity):
    dp = [0] * (capacity + 1)
    for curr_capacity in range(capacity+1):
        if weights[0] <= curr_capacity:
            dp[curr_capacity] = profits[0]

    print(0, dp)

    # 1 in the range cuz we already calculate the first row for the first item
    # and we will be incorrecting summing when curr_item = 0 and on top of that
    # we will be having dp[negative number] so it will become a mess XD
    for curr_item in range(1,len(profits)):
        for curr_capacity in range(capacity, -1, -1):
            include_curr_item = 0
            if weights[curr_item] <= curr_capacity:
                include_curr_item = profits[curr_item] + dp[curr_capacity - weights[curr_item]]
            not_include_curr_item = dp[curr_capacity]
            dp[curr_capacity] = max(include_curr_item, not_include_curr_item)
        print(curr_item, dp)

    return dp[-1]


import unittest

class TestKnapsack(unittest.TestCase):
    def test_knapsack(self):
        profits = [1,6,10,16]
        weights = [1,2,3,5]
        capacity = 7
        self.assertEqual(knapsack_bottom_up_1row(profits, weights, capacity), 22)
        profits = [4,5,3,7]
        weights = [2,3,1,4]
        capacity = 5
        self.assertEqual(knapsack_bottom_up_1row(profits, weights, capacity), 10)

def main():
    test = TestKnapsack()
    test.test_knapsack()


main()
