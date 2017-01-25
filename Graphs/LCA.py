"""
Find the least common ancestor of two nodes in a binary tree. Handle the case when one or both
the nodes may be absent from the tree.
"""


class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def lca(root, p, q):
    if root is None:
        return None

    found = [False, False]
    result = lca_helper(root, p, q, found)

    if (found[0] and found[1]) or (found[0] and find(root, q)) or (found[1] and find(root, p)):
        return result
    return None


def lca_helper(root, p, q, found):
    if root is None:
        return None
    if root is p:
        found[0] = True
        return root
    if root is q:
        found[1] = True
        return root
    left_lca = lca_helper(root.left, p, q, found)
    right_lca = lca_helper(root.right, p, q, found)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca


def find(root, n):
    if root is None:
        return False
    return root is n or find(root.left, n) or find(root.right, n)
