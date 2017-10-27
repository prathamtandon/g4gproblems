"""
Given a binary tree, find the size of largest independent set. LIS is a subset of nodes of the tree
such that there is no edge between any two nodes in the set.
"""


class Node:

    def __init__(self, key=0, lis=0, left=None, right=None):
        self.key = key
        self.lis = lis
        self.left = left
        self.right = right


def longest_independent_set(root):

    if root is None:
        return 0

    if root.left is None and root.right is None:
        root.lis = 1
        return 1

    if root.lis != 0:
        return root.lis

    lis_excl = longest_independent_set(root.left) + longest_independent_set(root.right)

    lis_incl = 1
    if root.left is not None:
        lis_incl += longest_independent_set(root.left.left) + longest_independent_set(root.left.right)
    if root.right is not None:
        lis_incl += longest_independent_set(root.right.left) + longest_independent_set(root.right.right)

    root.lis = max(lis_incl, lis_excl)
    return root.lis
