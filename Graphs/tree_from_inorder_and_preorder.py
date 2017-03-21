import unittest
"""
Given inorder and preorder traversal, construct the corresponding binary tree.
Input:
Inorder: D B E A F C
Preorder: A B D E C F
Output:
         A
       /   \
     /       \
    B         C
   / \        /
 /     \    /
D       E  F
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTreeFromPreorderAndInorder:
    def __init__(self, inorder, preorder):
        self.inorder = inorder
        self.preorder = preorder

    def build_tree(self):
        return self.build_tree_recursive(self.inorder)

    def build_tree_recursive(self, inorder):
        if not inorder:
            return None
        root = Node(self.preorder[0])
        self.preorder = self.preorder[1:]

        root_inorder_index = inorder.index(root.data)
        root.left = self.build_tree_recursive(inorder[:root_inorder_index])
        root.right = self.build_tree_recursive(inorder[root_inorder_index+1:])

        return root


class TestBinaryTree(unittest.TestCase):

    def test_inorder_preorder_to_tree(self):
        inorder = ['D', 'B', 'E', 'A', 'F', 'C']
        preorder = ['A', 'B', 'D', 'E', 'C', 'F']

        binaryTree = BinaryTreeFromPreorderAndInorder(inorder, preorder)
        root = binaryTree.build_tree()

        self.assertEqual(root.data, 'A')
        self.assertEqual(root.left.data, 'B')
        self.assertEqual(root.right.data, 'C')
        self.assertEqual(root.left.left.data, 'D')
        self.assertEqual(root.left.right.data, 'E')
        self.assertEqual(root.right.left.data, 'F')

