import unittest
"""
Given a binary tree, we need to find maximum value we can get by subtracting
value of node B from value of node A, where A and B are two nodes of the binary tree
and A is ancestor of B. Expected time complexity is O(n).
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def add_left_child(self, data):
        self.left = Node(data)
        return self.left

    def add_right_child(self, data):
        self.right = Node(data)
        return self.right


class BinaryTree:

    def __init__(self, root):
        self.root = root
        self.max_difference = -float('inf')

    def max_difference_node_and_ancestor(self):
        self.max_min_in_subtree(self.root)
        return self.max_difference

    def max_min_in_subtree(self, node):
        if node is None:
            return float('inf'), -float('inf')

        left_min, left_max = self.max_min_in_subtree(node.left)
        right_min, right_max = self.max_min_in_subtree(node.right)

        if node.left:
            self.max_difference = max(self.max_difference, node.data - left_min, node.data - left_max)
        if node.right:
            self.max_difference = max(self.max_difference, node.data - right_min, node.data - right_max)

        return min(node.data, left_min, right_min), max(node.data, left_max, right_max)


class TestBinaryTree(unittest.TestCase):

    def test_max_difference(self):
        root = Node(8)
        root.left = Node(3)
        root.left.left = Node(1)
        root.left.right = Node(6)
        root.left.right.left = Node(4)
        root.left.right.right = Node(7)
        root.right = Node(10)
        root.right.right = Node(14)
        root.right.right.left = Node(13)

        binary_tree = BinaryTree(root)

        self.assertEqual(binary_tree.max_difference_node_and_ancestor(), 7)



