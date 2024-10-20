from __future__ import annotations
from dataclasses import dataclass
from heapq import heappush, heappop

@dataclass
class Node:
    value: int
    next: Node | None = None
    # the /
    #   It signifies the end of the positional only parameters, 
    #   parameters you cannot use as keyword parameters
    # for assertEqual to work
    def __eq__(self, other, /) -> bool:
        return self.value == other.value
    # to insert the node in the heap and not just the node.value
    def __lt__(self, other):
        return self.value <= other.value

def merge_lists(lists):
    min_heap = []
    for node in lists:
        if node:
            heappush(min_heap, node)

    head, tail = None, None
    while min_heap:
        node = heappop(min_heap)
        if not tail:
            head = tail = node
        else:
            tail.next = node
            tail = tail.next

        if node.next:
            heappush(min_heap, node.next)

    print(head)
    return head


"""
L0=[2, 6*, 8], L1=[3, 6*, 7], L2=[1, 3, 4*]
res
[1]
heap
[(2, 0), (3, 1), (3, 2)]


"""


import unittest

class TestMergeLists(unittest.TestCase):
    def test_merge_lists(self):
        l1 = Node(2, Node(6, Node(8)))
        l2 = Node(3, Node(6, Node(7)))
        l3 = Node(1, Node(3, Node(4)))
        lists = [l1,l2,l3]
        self.assertEqual(merge_lists(lists),
                         Node(1, Node(2, Node(3, Node(3, Node(4, Node(6, Node(5, Node(7, Node(8))))))))))

def main():
    test = TestMergeLists()
    test.test_merge_lists()


main()
