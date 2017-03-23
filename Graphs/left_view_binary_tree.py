"""
Print the left view of binary tree. These are the nodes which are visible if
binary tree is viewed from left direction.
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.result = []
        self.max_level = -1

    def left_view(self):
        self.left_view_recursive(self.root, 0)
        return self.result

    def left_view_recursive(self, node, level):
        if not node:
            return

        if self.max_level < level:
            self.result.append(node.data)
            self.max_level = level

        self.left_view_recursive(node.left, level+1)
        self.left_view_recursive(node.right, level+1)
