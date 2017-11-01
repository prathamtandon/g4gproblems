"""
Given a binary tree, print boundary nodes of binary tree in anti-clockwise order starting from root.
"""

"""
Approach:
1. Print left boundary (print node.data before any of its children)
2. Print leaf nodes for left subtree.
3. Print leaf nodes for right subtree.
4. Print right boundary (print node.data after both of its children)
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_left_boundary(node):
    if node.left:
        print node.data
        print_left_boundary(node.left)
    elif node.right:
        print node.data
        print_left_boundary(node.right)


def print_right_boundary(node):
    if node.left:
        print_right_boundary(node.left)
        print node.data
    elif node.right:
        print_right_boundary(node.right)
        print node.data


def print_leaves(node):
    if node:
        print_leaves(node.left)
        if not node.left and not node.right:
            print node.data
        print_leaves(node.right)


def print_boundary(node):
    print_left_boundary(node)
    print_leaves(node.left)
    print_leaves(node.right)
    print_right_boundary(node.right)


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)

    print_boundary(root)

