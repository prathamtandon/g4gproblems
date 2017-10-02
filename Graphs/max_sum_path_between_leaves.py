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
        if not node:
            return -float('inf')

        lPath = self.max_sum_path_btw_leaves(node.left)
        rPath = self.max_sum_path_btw_leaves(node.right)

        # compute sum of path between leaf nodes passing through this node
        temp = 0
        if node.left:
            temp += lPath
        if node.right:
            temp += rPath
        temp += node.data

        # static variable to track the overall result
        BinaryTree.result = max(BinaryTree.result, temp)

        # compute maximum sum of path from this node to a leaf node.
        if lPath == -float('inf') and rPath == -float('inf'):
            return node.data

        return node.data + max(lPath, rPath)
