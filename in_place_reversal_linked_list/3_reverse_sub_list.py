class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

    def str_list(self) -> str:
        temp = self
        repr = ""
        while temp:
            repr += str(temp.value) + " "
            temp = temp.next

        return repr


def reverse_sub_list(head, p, q) -> Node | None: 
    if p == q:
        return head

    prev, curr = None, head
    i = 0
    while curr and i < p - 1:
        prev = curr
        curr = curr.next
        i += 1

    last_node_first_part = prev
    last_node_sub_list = curr

    i = 0
    while curr.next and i < q - 1:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        i += 1

    if last_node_first_part:
        last_node_first_part.next = prev
    else:
        # this means p == 1 i.e. we are changing the first node (head)
        # of the linked list
        head = prev
    
    last_node_sub_list.next = curr

    return head


import unittest


class TestReverse(unittest.TestCase):
    def setUp(self) -> None:
        self.head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
        self.expected = Node(1, Node(4, Node(3, Node(2, Node(5)))))

    def test_reverse(self):
        print("Original list: ", end=" ")
        print(self.head.str_list())

        print("Reversed list: ", end=" ")
        result = reverse_sub_list(self.head, 2, 4)
        print(result.str_list())

        self.assertEqual(result.str_list(), self.expected.str_list())


if __name__ == "__main__":
    unittest.main()

