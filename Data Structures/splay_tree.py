import unittest
"""
A splay tree is a type of balanced binary search tree.  Structurally, it is
identical to an ordinary binary search tree; the only difference is in the
algorithms for finding, inserting, and deleting entries.

All splay tree operations run in O(log n) time _on_average_, where n is the
number of entries in the tree.  Any single operation can take Theta(n) time in
the worst case.  But any sequence of k splay tree operations, with the tree
initially empty and never exceeding n items, takes O(k log n) worst-case time.

Splay trees are designed to give especially fast access to entries that have
been accessed recently, so they really excel in applications where a small
fraction of the entries are the targets of most of the find operations.
In other words, the search operation on keys is not uniformly distributed over all
the keys. Instead, major percentage of search is focused on a very small fraction of overall keys.
"""


class SplayTree:

    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.key = key

    def __init__(self):
        self.root = None

    def create_node(self, key):
        return self.Node(key)

    def right_rotate(self):
        self.root = self.right_rotate_helper(self.root)

    def right_rotate_helper(self, root):
        new_root = root.left
        root.left = new_root.right
        new_root.right = root
        return new_root

    def left_rotate(self):
        self.root = self.left_rotate_helper(self.root)

    def left_rotate_helper(self, root):
        new_root = root.right
        root.right = new_root.left
        new_root.left = root
        return new_root

    def splay(self, key):
        self.root = self.splay_helper(self.root, key)

    def splay_helper(self, root, key):
        if root.key == '' or root.key == key:
            return root

        if key < root.key:
            if root.left is None:
                return root
            # Zig Zig rotation
            if key < root.left.key:
                root.left.left = self.splay_helper(root.left.left, key)
                root = self.right_rotate_helper(root)
            # Zig Zag rotation
            elif key > root.left.key:
                root.left.right = self.splay_helper(root.left.right, key)
                if root.left.right is not None:
                    root.left = self.left_rotate_helper(root.left)

            return root if root.left is None else self.right_rotate_helper(root)

        else:
            if root.right is None:
                return root
            # Zag Zag rotation
            if key > root.right.key:
                root.right.right = self.splay_helper(root.right.right, key)
                root = self.left_rotate_helper(root)
            # Zag Zig rotation
            elif key < root.right.key:
                root.right.left = self.splay_helper(root.right.left, key)
                if root.right.left is not None:
                    root.right = self.right_rotate_helper(root.right)

            return root if root.right is None else self.left_rotate_helper(root)

    def search(self, key):
        self.splay(key)


class TestSplayTrees(unittest.TestCase):

    def test_splay_tree_search(self):
        st = SplayTree()
        st.root = st.create_node(100)
        st.root.left = st.create_node(50)
        st.root.right = st.create_node(200)
        st.root.left.left = st.create_node(40)
        st.root.left.left.left = st.create_node(30)
        st.root.left.left.left.left = st.create_node(20)

        self.assertEqual(st.root.key, 100)
        st.search(20)
        self.assertEqual(st.root.key, 20)
