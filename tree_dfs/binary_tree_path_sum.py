from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

def sum(root, s):
    return sum_rec(root, s, 0)

def sum_rec(root, s, total):
    if not root:
        if s == total:
            return True
        return False

    return sum_rec(root.left, s, total + root.value) or \
        sum_rec(root.right, s, total + root.value)


import unittest

class TestSumPath(unittest.TestCase):
    def test_sum_path(self):
        tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
        self.assertTrue(sum(tree, 10))

if __name__ == '__main__':
    unittest.main()
