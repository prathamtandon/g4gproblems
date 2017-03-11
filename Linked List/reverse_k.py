"""
Given a linked list, write a function to reverse every k nodes.
Input: 1->2->3->4->5->6->7->8->NULL and k = 3
Output: 3->2->1->6->5->4->8->7->NULL
"""

"""
Approach:
1. First reverse the first k items.
2. Let prev be the previous node and next be next node in reversed list.
3. Make next point to reverse of remainder of items. Return prev as new head.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_k(head, k):

    if not head or k == 0 or k == 1:
        return head

    prev = None
    cur = head
    count = 0

    while cur and count < k:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
        count += 1

    if cur:
        head.next = reverse_k(cur, k)

    return prev


def print_ll(head):
    result = []
    cur = head
    while cur:
        result.append(cur.data)
        cur = cur.next
    print result


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print_ll(head)
    print_ll(reverse_k(head, 5))
