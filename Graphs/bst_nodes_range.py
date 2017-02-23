import unittest
"""
Given a BST and a range, count the number of nodes in the BST that lie in the given
range.
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def get_count_of_nodes(root, low, high):
    if root is None:
        return 0
    if low <= root.data <= high:
        return 1 + get_count_of_nodes(root.left, low, high) + get_count_of_nodes(root.right, low, high)
    elif root.data > low:
        return get_count_of_nodes(root.left, low, high)
    else:
        return get_count_of_nodes(root.right, low, high)


class TestCountOfNodes(unittest.TestCase):

    def test_count_of_nodes(self):
        root = Node(10)
        root.left = Node(5)
        root.left.left = Node(1)
        root.right = Node(50)
        root.right.left = Node(40)
        root.right.right = Node(100)
        self.assertEqual(get_count_of_nodes(root, 5, 45), 3)
