import unittest
"""
Given two BSTs, return a list of elements from both BSTs in sorted order.
"""

"""
Approach: The idea is to use iterative inorder traversal and maintain two stacks, one for each BST.
NOTE: To understand this code, first understand how iterative inorder traversal works.
"""


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def inorder(root, result):
    if root is not None:
        inorder(root.left, result)
        result.append(root.key)
        inorder(root.right, result)


def merge_bst(root1, root2, result):
    if root1 is None:
        inorder(root2, result)
        return
    if root2 is None:
        inorder(root1, result)
        return
    stack1 = []
    stack2 = []
    current1 = root1
    current2 = root2

    while current1 is not None or len(stack1) > 0 or current2 is not None or len(stack2) > 0:
        if current1 is not None or current2 is not None:
            if current1 is not None:
                stack1.insert(0, current1)
                current1 = current1.left
            if current2 is not None:
                stack2.insert(0, current2)
                current2 = current2.left
        else:
            if len(stack1) == 0:
                current2 = stack2.pop(0)
                inorder(current2, result)
                return
            if len(stack2) == 0:
                current2 = stack1.pop(0)
                inorder(current2, result)
                return
            current1 = stack1.pop(0)
            current2 = stack2.pop(0)

            if current1.key < current2.key:
                result.append(current1.key)
                current1 = current1.right
                stack2.insert(0, current2)
                current2 = None
            else:
                result.append(current2.key)
                current2 = current2.right
                stack1.insert(0, current1)
                current1 = None


class TestMergeBSTs(unittest.TestCase):

    def test_merge_bst(self):
        root1 = Node(3)
        root1.left = Node(1)
        root1.right = Node(5)

        root2 = Node(4)
        root2.left = Node(2)
        root2.right = Node(6)

        result = []
        merge_bst(root1, root2, result)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
