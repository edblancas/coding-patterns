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
    q = deque([root])
    level = 1
    new_level = 0
    res = deque()
    while q:
        sub_res = []
        new_level = 0
        for _ in range(level):
            node = q.popleft()
            sub_res.append(node.value)
            if node.left:
                q.append(node.left)
                new_level += 1
            if node.right:
                q.append(node.right)
                new_level += 1

        res.appendleft(sub_res)
        level = new_level

    return res
    

import unittest


class TestDFSLevel(unittest.TestCase):
    def test_dfs_level(self):
        tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
        self.assertEqual(list(dfs(tree)), list(reversed([[1], [2, 3], [4, 5, 6, 7]])))

        tree2 = Node(12, Node(7, Node(9)), Node(1, Node(10), Node(5)))
        self.assertEqual(list(dfs(tree2)), list(reversed([[12], [7, 1], [9, 10, 5]])))


if __name__ == "__main__":
    unittest.main()
