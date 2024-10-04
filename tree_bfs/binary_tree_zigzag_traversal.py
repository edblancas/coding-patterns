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
    if not root: return []

    q = deque([root])
    res = []
    left_to_right = True
    while q:
        level_size = len(q)
        sub = deque()
        for _ in range(level_size):
            n = q.popleft()
            if left_to_right:
                sub.append(n.value)
            else:
                sub.appendleft(n.value)

            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        res.append(list(sub))
        left_to_right = not left_to_right

    return res




import unittest


class TestDFSLevel(unittest.TestCase):
    def test_dfs_level(self):
        tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
        self.assertEqual(dfs(tree),[[1], [3,2], [4, 5, 6, 7]])

        tree2 = Node(12, Node(7, Node(9)), Node(1, Node(10), Node(5)))
        self.assertEqual(dfs(tree2), [[12], [1,7], [9, 10, 5]])


if __name__ == "__main__":
    unittest.main()
