import unittest
"""
Diameter of a binary tree is number of nodes on longest path between any two leaves in the tree.
Recursive definition of diameter =
max(diameter of left subtree, diameter of right subtree, 1 + height of left subtree + height of right subtree).
The first two cases are when diameter path does not include current node and third case is when diameter path
includes current node.
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def diameter(self):
        return self.diameter_of_subtree(self.root)[0]

    def diameter_of_subtree(self, node):
        if node is None:
            return -float('inf'), 0

        left_diameter, left_height = self.diameter_of_subtree(node.left)
        right_diameter, right_height = self.diameter_of_subtree(node.right)

        height = 1 + max(left_height, right_height)

        return max(left_diameter, right_diameter, 1 + left_height + right_height), height


class TestBinaryTree(unittest.TestCase):

    def test_diameter(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)

        binary_tree = BinaryTree(root)
        self.assertEqual(binary_tree.diameter(), 4)
