import unittest
"""
Construct tree from given inorder and preorder traversals.
Input:
Inorder: D B E A F C
Preorder: A B D E C F
In a preorder sequence, leftmost element is root of tree. So, we know 'A' is root from given preorder sequence.
By searching 'A' in inorder sequence, we can find out all elements on left side of 'A' are in left subtree
and all elements on right are in right subtree.
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def build_tree_helper(inorder, preorder, in_start, in_end):

    if in_start > in_end:
        return None

    tree_node = Node(preorder[build_tree_helper.pre_index])
    build_tree_helper.pre_index += 1

    if in_start == in_end:
        return tree_node

    in_index = search(inorder, in_start, in_end, tree_node.data)

    tree_node.left = build_tree_helper(inorder, preorder, in_start, in_index - 1)
    tree_node.right = build_tree_helper(inorder, preorder, in_index + 1, in_end)

    return tree_node


def search(arr, start, end, ele):
    for i in range(start, end+1):
        if arr[i] == ele:
            return i

    return -1


def build_tree(inorder, preorder):
    build_tree_helper.pre_index = 0
    n = len(inorder)
    return build_tree_helper(inorder, preorder, 0, n-1)


class TestBuildTree(unittest.TestCase):

    def test_build_tree(self):
        inorder = ['D', 'B', 'E', 'A', 'F', 'C']
        preorder = ['A', 'B', 'D', 'E', 'C', 'F']
        root = build_tree(inorder, preorder)
        self.assertEqual(root.data, 'A')
        self.assertEqual(root.left.data, 'B')
        self.assertEqual(root.right.data, 'C')
        self.assertEqual(root.left.left.data, 'D')
        self.assertEqual(root.left.right.data, 'E')
        self.assertEqual(root.right.left.data, 'F')
