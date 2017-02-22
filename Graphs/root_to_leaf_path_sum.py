import unittest
"""
Given a binary tree, where every node value is a digit from 1-9. Find the sum of all the numbers which
are formed from root to leaf paths.
"""


class Node:

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


class Result:

    def __init__(self, data, level):
        self.data = data
        self.level = level


def root_to_leaf_path_sum(root, level):
    if root is None:
        return []
    if root.left is None and root.right is None:
        result = Result(root.key, level)
        return [result]
    left_paths = root_to_leaf_path_sum(root.left, level+1)
    right_paths = root_to_leaf_path_sum(root.right, level+1)
    total_paths = left_paths + right_paths
    for path in total_paths:
        path.data += 10 ** (path.level - level) * root.key
    return total_paths


def root_to_leaf(root):
    paths = root_to_leaf_path_sum(root, 0)
    if len(paths) == 0:
        return 0
    return sum([x.data for x in paths])


class TestRootToLeaf(unittest.TestCase):

    def test_root_to_leaf(self):
        root = Node(6)
        root.left = Node(3)
        root.right = Node(5)
        root.left.left = Node(2)
        root.left.right = Node(5)
        root.left.right.left = Node(7)
        root.left.right.right = Node(4)
        root.right.right = Node(4)

        self.assertEqual(root_to_leaf(root), 13997)
