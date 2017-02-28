"""
Write a program to check if a given binary tree is bst or not.
"""

"""
Approach 1:
1. For each node, check that node's value is greater than max_value in its left subtree and smaller than
   min_value in its right subtree.
2. This approach is not efficient as each node is traversed multiple times.

Approach 2:
1. We use two variables, min and max, to track the range in which the current node's data should lie.
2. Initially, min = -INF and max = INF.
3. At each node, when we go to its left subtree, we make max = node.data and when we go to its right subtree
   we make min = node.data

Approach 3:
1. We can do an in-order traversal of the tree and see if the output is sorted.
2. A space optimization is, we only keep track of previously seen node's value. If current node's value
   is less than previous node's value, binary tree is not BST.

Below, Approach 2 is implemented.
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def is_bst(node):
    if node is None:
        return True
    return is_bst_helper(node, -float('inf'), float('inf'))


def is_bst_helper(node, min_val, max_val):
    if node is None:
        return True
    if node.data < min_val or node.data > max_val:
        return False
    return is_bst_helper(node.left, min_val, node.data) and is_bst_helper(node.right, node.data, max_val)
