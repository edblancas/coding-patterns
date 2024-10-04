from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

def sum(root, s):
    return sum_rec(root, s, [], [], 0)

def sum_rec(root, s, path, total, sum):
    if root and not root.left and not root.right:
        if s == sum + root.value:
            total.append(list(path + [root.value]))
            return
        return

    path.append(root.value)
    sum_rec(root.left, s, path, total, sum + root.value) 
    sum_rec(root.right, s, path, total, sum + root.value)
    path.pop()
    return total


import unittest

class TestSumPath(unittest.TestCase):
    def test_sum_path(self):
        tree = Node(1, Node(7, Node(4), Node(5)), Node(9, Node(2), Node(7)))
        self.assertEqual(sum(tree, 12), [[1,7,4], [1,9,2]])

if __name__ == '__main__':
    unittest.main()
