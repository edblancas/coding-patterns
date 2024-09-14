# Given the head of a Singly LinkedList, write a function to determine if the 
# LinkedList has a cycle in it or not.
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    value: int
    next: Node | None = None

# time O(n), space O(1)
def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def find_cycle_length(head):
    slow = head
    fast = head
    length = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # simpler and is alway better to do it this way in interviews
            return calculate_cycle_length(slow)
            # same but more confusing
            # fast = fast.next
            # length += 1
            # while slow != fast:
            #     fast = fast.next
            #     length += 1
            # return length
    return None

def calculate_cycle_length(node):
    length = 0
    curr = node
    while True:
        curr = curr.next
        length += 1
        if curr == node:
            break
    return length

import unittest

class TestCycle(unittest.TestCase):
    def setUp(self) -> None:
        self.head = Node(2, Node(4, Node(6, Node(8, Node(10)))))
        node6 = Node(6)
        node3 = Node(3, Node(4, Node(5, node6)))
        node6.next = node3
        self.head2 = Node(1, Node(2, node3))

    def test_has_cycle(self):
        self.assertFalse(has_cycle(self.head))
        self.assertTrue(has_cycle(self.head2))

    def test_find_cycle_length(self):
        self.assertEqual(find_cycle_length(self.head2), 4)
        self.assertEqual(find_cycle_length(self.head), None)

if __name__ == '__main__':
    unittest.main()
