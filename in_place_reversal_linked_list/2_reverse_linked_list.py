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


def reverse_rec(head) -> Node:
    if not head.next:
        return head

    new_head = reverse_rec(head.next)
    head.next.next = head
    head.next = None

    return new_head


def reverse_iter(head) -> Node | None:
    curr = head
    prev = None
    # is more clear
    # while curr is not None:
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


def reverse(head) -> Node | None:
    return reverse_iter(head)


import unittest


class TestReverse(unittest.TestCase):
    def setUp(self) -> None:
        self.head = Node(2, Node(4, Node(6, Node(8, Node(10)))))
        self.expected = Node(10, Node(8, Node(6, Node(4, Node(2)))))

    def test_reverse(self):
        print("Original list: ", end=" ")
        print(self.head.str_list())

        print("Reversed list: ", end=" ")
        result = reverse(self.head)
        print(result.str_list())

        self.assertEqual(result.str_list(), self.expected.str_list())


if __name__ == "__main__":
    unittest.main()
