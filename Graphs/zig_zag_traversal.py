import unittest
"""
Write a program to traverse a binary tree in zig-zag fashion.
"""


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def zig_zag_helper(stack1, stack2, left_to_right, result):

    if len(stack1) == 0 and len(stack2) == 0:
        return

    if left_to_right:
        while len(stack2) > 0:
            node = stack2.pop(0)
            result.append(node.key)
            if node.left is not None:
                stack1.insert(0, node.left)
            if node.right is not None:
                stack1.insert(0, node.right)
    else:
        while len(stack1) > 0:
            node = stack1.pop(0)
            result.append(node.key)
            if node.right is not None:
                stack2.insert(0, node.right)
            if node.left is not None:
                stack2.insert(0, node.left)

    return zig_zag_helper(stack1, stack2, not left_to_right, result)


def zig_zag_traversal(root):

    stack1 = [root]
    stack2 = []
    result = []
    zig_zag_helper(stack1, stack2, False, result)
    return result


class TestZigZag(unittest.TestCase):

    def test_zig_zag(self):
        root = Node(10)
        root.left = Node(5)
        root.left.left = Node(3)
        root.left.right = Node(-1)
        root.right = Node(6)
        root.right.left = Node(11)
        root.right.right = Node(6)
        self.assertEqual(zig_zag_traversal(root), [10, 5, 6, 6, 11, -1, 3])
