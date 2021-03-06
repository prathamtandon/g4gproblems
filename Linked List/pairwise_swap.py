"""
Given a singly linked list, write a function to swap elements pairwise.
Input: 1->2->3->4->5->6->7
Output: 2->1->4->3->6->5->7
Input: 1->2->3->4
Output: 2->1->4->3
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def pairwise_swap(head):
    if not head or not head.next:
        return head

    temp = head.next
    next = temp.next
    temp.next = head
    head.next = pairwise_swap(next)
    return temp


def print_ll(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    print result


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    print_ll(head)
    print_ll(pairwise_swap(head))
