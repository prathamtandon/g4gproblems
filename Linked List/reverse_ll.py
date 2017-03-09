"""
Reverse a linked list. Expected time complexity is O(n) and space complexity is O(1).
"""


def reverse_ll(node):

    prev = None
    cur = node

    while cur is not None:
        temp = cur.right
        cur.right = prev
        prev = cur
        cur = temp

    return prev


def print_ll(node):

    result = []
    while node is not None:
        result.append(node.key)
        node = node.right

    print result


class Node:
    def __init__(self, key, right=None):
        self.key = key
        self.right = right


if __name__ == '__main__':
    node = Node(1)
    node.right = Node(2)
    node.right.right = Node(3)
    node.right.right.right = Node(4)
    node.right.right.right.right = Node(5)

    print_ll(node)
    print_ll(reverse_ll(node))
