import unittest
"""
Write a function to connect all adjacent nodes at same level in binary tree.
"""


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.next_right = None


def connect_level(root):

    if root is None:
        return None
    left_answer = connect_level(root.left)
    right_answer = connect_level(root.right)
    if left_answer is not None and right_answer is not None:
        left_answer.next_right = right_answer
    a = None
    b = None
    c = None
    d = None
    if left_answer is not None:
        a = left_answer.left
        b = left_answer.right
    if right_answer is not None:
        c = right_answer.left
        d = right_answer.right
    if a is not None and b is None:
        if c is not None:
            a.next_right = c
        else:
            a.next_right = d
    elif b is not None:
        if c is not None:
            b.next_right = c
        else:
            b.next_right = d
    return root


class TestLevelConnection(unittest.TestCase):

    def test_level(self):
        root = Node(10)
        root.left = Node(3)
        root.right = Node(5)
        root.left.left = Node(4)
        root.left.right = Node(1)
        root.right.right = Node(2)
        root = connect_level(root)
        self.assertEqual(root.left.next_right, root.right)
        self.assertEqual(root.left.left.next_right, root.left.right)
        self.assertEqual(root.left.right.next_right, root.right.right)
