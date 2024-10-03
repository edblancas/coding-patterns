"""
queue       =h[4,5]t
range=
lvl size    =2
new lvl size=4
lvl res     =[2,3]
res         =[[1][2,3]]
"""

from __future__ import annotations
from dataclasses import dataclass
from collections import deque


@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None


def dfs(root): 
    level_size = 1
    queue = deque([root])
    result = []

    while queue:
        new_level_size = 0
        level_res = []
        for _ in range(level_size):
            node = queue.popleft()
            level_res.append(node.value)
            if node.left:
                new_level_size += 1
                queue.append(node.left)
            if node.right:
                new_level_size += 1
                queue.append(node.right)

        result.append(level_res)
        level_size = new_level_size

    return result



import unittest


class TestDFSLevel(unittest.TestCase):
    def test_dfs_level(self):
        tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
        self.assertEqual(dfs(tree), [[1], [2, 3], [4, 5, 6, 7]])

        tree2 = Node(12, Node(7, Node(9)), Node(1, Node(10), Node(5)))
        self.assertEqual(dfs(tree2), [[12], [7, 1], [9, 10, 5]])


if __name__ == "__main__":
    unittest.main()
