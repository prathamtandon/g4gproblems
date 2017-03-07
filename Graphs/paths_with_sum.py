import unittest
"""
You are given a binary tree in which each node contains an integer value (which might be positive or negative)
Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or
end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
"""

"""
Approach:
1. The idea is to keep a running sum: sum of all nodes from root to current node.
2. Maintain a hashtable of running sum values, and increment the hashtable if running sum is already present.
3. Now, say we are looking for target_sum. Now, if running_sum - target_sum is present in hashtable,
   it means there is a path ending in current node, with sum = target_sum. Number of such paths = value in hashtable.
4. We recursively do this for left and right subtrees of current node.
5. Once, we have done exploring a node, we decrement running_sum value by 1 in the hashtable, since this node
   cannot be reached from any other node in the tree now, hence no need of keeping the path ending at it.
"""

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


def paths_with_sum_helper(node, running_sum, target_sum, table):

    if node is None:
        return 0

    total_paths = 0
    running_sum += node.key

    if running_sum in table:
        table[running_sum] += 1
    else:
        table[running_sum] = 1

    if running_sum - target_sum in table:
        total_paths = table[running_sum - target_sum]

    total_paths += paths_with_sum_helper(node.left, running_sum, target_sum, table)
    total_paths += paths_with_sum_helper(node.right, running_sum, target_sum, table)

    table[running_sum] -= 1
    if table[running_sum] == 0:
        del table[running_sum]
    return total_paths


def paths_with_sum(node, target_sum):
    table = dict()
    # needed if target_sum starts at root
    table[0] = 1
    return paths_with_sum_helper(node, 0, target_sum, table)


class TestPathsWithSum(unittest.TestCase):

    def test_paths_with_sum(self):
        root = Node(10)
        root.left = Node(5)
        root.left.left = Node(3)
        root.left.left.left = Node(3)
        root.left.left.right = Node(-2)
        root.left.right = Node(1)
        root.left.right.right = Node(2)
        root.right = Node(-3)
        root.right.right = Node(11)

        self.assertEqual(paths_with_sum(root, 8), 3)
