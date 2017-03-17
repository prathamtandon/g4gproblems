"""
Find inorder successor of node without using parent pointers.
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root):
        self.root = root

    def min_in_subtree(self, node):
        if not node:
            return None
        while node.left:
            node = node.left
        return node.data

    def inorder_successor(self, node):
        if node.right:
            return self.min_in_subtree(node)
        successor = None
        temp = self.root
        while temp:
            if temp.data > node.data:
                successor = temp
                temp = temp.left
            elif temp.data < node.data:
                temp = temp.right
            else:
                break

        return successor.data if successor else None
