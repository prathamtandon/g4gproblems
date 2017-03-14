"""
Given a singly linked list, swap kth node from beginning with kth node from end.
Swapping of data is not allowed, only pointers should be changed.
"""


def swap_kth_nodes(head, k):
    n = count_nodes(head)

    if k > n:
        return head

    # kth from beginning == kth from end
    if n == 2*k-1:
        return head

    # find kth node from beginning
    prev_x = None
    x = head
    for i in range(1, k):
        prev_x = x
        x = x.next

    # find kth node from end: (n-k+1)st from beginning
    prev_y = None
    y = head
    for i in range(1, n-k+1):
        prev_y = y
        y = y.next

    # Update prev pointers
    if prev_x:
        prev_x.next = y
    if prev_y:
        prev_y.next = x

    # Update next pointers
    temp = x.next
    x.next = y.next
    y.next = temp

    # Update head pointer
    if k == 1:
        head = y
    if k == n:
        head = x

    return head


def count_nodes(head):
    cur = head
    count = 0
    while cur:
        count += 1
        cur = cur.next
    return count


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_ll(head):
    cur = head
    result = []
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

    print_ll(head)
    print_ll(swap_kth_nodes(head, 5))

