"""
Remove duplicates from a sorted linked list. The list should be traversed at once.
Input: 11->11->11->21->43->43->60
Output: 11->21->43->60
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_duplicates(head):
    if head is None:
        return
    prev = head
    cur = head.next
    while cur:
        next = cur.next
        if prev.data == cur.data:
            prev.next = next
        else:
            prev = cur
        cur = next

    return head


def print_ll(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    print result


if __name__ == '__main__':
    head = Node(11)
    head.next = Node(11)
    head.next.next = Node(11)
    head.next.next.next = Node(21)
    head.next.next.next.next = Node(43)
    head.next.next.next.next.next = Node(43)
    head.next.next.next.next.next.next = Node(60)

    print_ll(head)
    print_ll(remove_duplicates(head))
