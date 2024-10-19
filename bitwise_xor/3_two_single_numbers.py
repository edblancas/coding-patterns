def find_single_numbers_me(nums):
    n1_xor_n2 = 0
    for n in nums:
        n1_xor_n2 ^= n

    print('xor nums=', n1_xor_n2)

    pos = 0
    bit = n1_xor_n2
    while bit:
        bit &= 1
        bit <<= 1
        pos += 1

    print('bit 1 pos --->', pos)

    n_with_pos_1 = 1 << pos

    print('--->', n_with_pos_1)

    ones = []
    zeros = []
    for n in nums:
        if n & n_with_pos_1 == n_with_pos_1:
            ones.append(n)
        else:
            zeros.append(n)

    print('ones', ones)
    print('zeros', zeros)

    res = []
    num = 0
    for n in ones:
        num ^= n
    res.append(num)
    num = 0
    for n in zeros:
        num ^= n
    res.append(num)

    return res


def find_single_numbers(arr):
    n1xn2 = 0
    for n in arr:
        n1xn2 ^= n

    firs1bit = 1
    while n1xn2 & firs1bit == 0:
        firs1bit <<= 1

    n1, n2 = 0, 0
    for n in arr:
        if n & firs1bit != 0:
            n1 ^= n
        else:
            n2 ^= n

    return [n1, n2]


import unittest

class TestFindSingleNumbers(unittest.TestCase):
    def test_find_single_numbers(self):
        self.assertEqual(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]), [6, 4])

def main():
    test = TestFindSingleNumbers()
    test.test_find_single_numbers()


main()
