import unittest
"""
Given a linked list with members sorted in ascending order, return a Balanced Binary Search Tree
having same data members as given linked list.
Input: 1->2->3
Output:    2
          / \
         1  3
"""

"""
Approach:
1. Idea is to first count the number of nodes in LinkedList. Say this value is n.
2. We then recursively construct the left subtree using the first n/2 nodes.
3. Then we create the root node and link it with left subtree.
4. We then recursively construct the right subtree using the last n/2 nodes.
5. Then we link root nodes with right subtree.
6. In each iteration, we move the head of linked list to next node in the list. So, the entire
   tree can be created in a single scan of the linked list.
"""

head = None


class LinkedListNode:
    def __init__(self, data, after=None):
        self.data = data
        self.after = after


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def size(h):
    result = 0
    while h is not None:
        result += 1
        h = h.after
    return result


def ll_to_bst(h):
    global head
    head = h
    return ll_to_bst_helper(size(head))


def ll_to_bst_helper(n):
    if n <= 0:
        return None
    left_subtree = ll_to_bst_helper(n/2)
    root = TreeNode(head.data)
    root.left = left_subtree
    global head
    head = head.after
    right_subtree = ll_to_bst_helper(n-n/2-1)
    root.right = right_subtree
    return root


class TestLLToBST(unittest.TestCase):

    def test_ll_to_bst_odd_length(self):
        h = LinkedListNode(1)
        h.after = LinkedListNode(2)
        h.after.after = LinkedListNode(3)
        h.after.after.after = LinkedListNode(4)
        h.after.after.after.after = LinkedListNode(5)
        h.after.after.after.after.after = LinkedListNode(6)
        h.after.after.after.after.after.after = LinkedListNode(7)
        root = ll_to_bst(h)
        self.assertEqual(root.data, 4)
        self.assertEqual(root.left.data, 2)
        self.assertEqual(root.right.data, 6)
        self.assertEqual(root.left.left.data, 1)
        self.assertEqual(root.left.right.data, 3)
        self.assertEqual(root.right.left.data, 5)
        self.assertEqual(root.right.right.data, 7)

    def test_ll_to_bst_even_length(self):
        h = LinkedListNode(1)
        h.after = LinkedListNode(2)
        h.after.after = LinkedListNode(3)
        h.after.after.after = LinkedListNode(4)
        root = ll_to_bst(h)
        self.assertEqual(root.data, 3)
        self.assertEqual(root.left.data, 2)
        self.assertEqual(root.right.data, 4)
        self.assertEqual(root.left.left.data, 1)
