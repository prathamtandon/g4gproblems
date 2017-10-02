"""
Given a binary tree, each node element contains a number. Find maximum possible sum
between two leaf nodes.
"""


"""
Approach:
1. We can do this in single traversal of the tree.
2. The idea is to return the maximum sum from a node to any leaf node from subtree rooted at that node.
3. Maximum sum between any two leaf nodes in a subtree rooted at some node will be the max between:
    Max sum from left subtree, Max sum from right subtree, Max sum path crossing through the node.
"""


class BinaryTree:

    def max_sum_path_btw_leaves(self, node):
        if node is None:
            return 0, 0

        lPath = self.max_sum_path_btw_leaves(node.left)
        rPath = self.max_sum_path_btw_leaves(node.right)

        # static variable to track the overall result
        BinaryTree.result = max(BinaryTree.result, node.data + lPath + rPath)

        return node.data + max(lPath, rPath)
