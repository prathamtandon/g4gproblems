import unittest
"""
The diameter of a tree is the number of nodes on the longest path between two leaves in the tree.
"""


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

"""
Diameter of root = max(diameter of root.left, diameter of root.right, 1+height(root.left)+height(root.right))
"""


def diameter(root):
    if root is None:
        return 0, 0
    ldiam, lheight = diameter(root.left)
    rdiam, rheight = diameter(root.right)
    return max(ldiam, rdiam, 1+lheight+rheight), 1+max(lheight, rheight)


class TestDiameter(unittest.TestCase):

    def test_diameter(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        self.assertEqual(diameter(root)[0], 4)
