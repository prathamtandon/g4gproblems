"""
Given a binary tree, convert it to BST. The conversion should be done in such a way
that keeps the original structure of binary tree.
Input:
          10
         /  \
        2    7
       / \
      8   4
Output:
          8
         /  \
        4    10
       / \
      2   7
Input:
          10
         /  \
        30   15
       /      \
      20       5
Output:
          15
         /  \
       10    20
       /      \
      5        30
"""

"""
Approach:
1. Do inorder traversal of tree and store it in a temp array.
2. Sort the temp array.
3. Do another inorder traversal, this time replace tree node values with values from sorted array.
Time complexity is O(nlog(n))
"""


def binary_to_bst(root):
    result = []
    inorder(root, result, False)
    result = sorted(result)
    inorder(root, result, True)


def inorder(root, result, result_to_bst):
    if root:
        inorder(root.left, result, result_to_bst)
        if result_to_bst:
            data = result.pop(0)
            root.data = data
        else:
            result.append(root.data)
        inorder(root.right, result, result_to_bst)


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

if __name__ == '__main__':
    root = Node(10)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(8)
    root.left.right = Node(4)

    binary_to_bst(root)
    assert root.data == 8
    assert root.left.data == 4
    assert root.right.data == 10
    assert root.left.left.data == 2
    assert root.left.right.data == 7
