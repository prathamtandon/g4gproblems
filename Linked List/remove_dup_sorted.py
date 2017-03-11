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
    current = head
    while current.next:
        if current.data == current.next.data:
            next_next = current.next.next
            current.next = None
            current.next = next_next
        else:
            current = current.next

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
