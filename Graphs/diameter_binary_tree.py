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
        self.height_of_subtree = 0


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def diameter(self):
        return self.diameter_of_subtree(self.root)

    def diameter_of_subtree(self, node):
        if node is None:
            return -float('inf')

        left_diameter = self.diameter_of_subtree(node.left)
        right_diameter = self.diameter_of_subtree(node.right)

        left_height = node.left.height_of_subtree if node.left else 0
        right_height = node.right.height_of_subtree if node.right else 0

        node.height_of_subtree = 1 + max(left_height, right_height)

        return max(left_diameter, right_diameter, 1 + left_height + right_height)


class TestBinaryTree(unittest.TestCase):

    def test_diameter(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)

        binary_tree = BinaryTree(root)
        self.assertEqual(binary_tree.diameter(), 4)
