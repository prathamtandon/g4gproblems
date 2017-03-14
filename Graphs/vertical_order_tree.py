import unittest
"""
Given a binary tree, find the vertical sum of nodes that are in same vertical line.
Print all sums through different vertical lines.
"""

"""
Approach:
1. A simple way is to calculate horizontal distance of every node in the tree.
2. If horizontal distance of root is hd, the for root.left it is hd-1 and for root.right it is hd+1.
3. We can use a hashtable with hd as key, and value as sum of all nodes with horizontal distance as given key.
4. A space optimized approach uses doubly linked list, and space complexity is O(V) where V is number of
   vertical lines.
NOTE: We can reuse the same class to represent LL and Tree nodes. node.left and node.prev are same while node.right
and node.next are same.
"""


class TNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def vertical_sum(root):
    llnode = TNode(0)
    vertical_sum_util(root, llnode)

    # llnode points to vertical sum of line passing through root, we move it to leftmost vertical line
    while llnode.left:
        llnode = llnode.left

    result = []
    while llnode:
        result.append(llnode.data)
        llnode = llnode.right

    return result


def vertical_sum_util(tnode, llnode):
    llnode.data += tnode.data
    # Recursively process left subtree
    if tnode.left:
        if not llnode.left:
            llnode.left = TNode(0)
            llnode.left.right = llnode
        vertical_sum_util(tnode.left, llnode.left)
    # Recursively process right subtree
    if tnode.right:
        if not llnode.right:
            llnode.right = TNode(0)
            llnode.right.left = llnode
        vertical_sum_util(tnode.right, llnode.right)


class TestVerticalOrder(unittest.TestCase):

    def test_vertical_order(self):
        root = TNode(1)
        root.left = TNode(2)
        root.right = TNode(3)
        root.left.left = TNode(4)
        root.left.right = TNode(5)
        root.right.left = TNode(6)
        root.right.right = TNode(7)

        self.assertEqual(vertical_sum(root), [4, 2, 12, 3, 7])
