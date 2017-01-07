import unittest
"""
Given a sorted array keys[0.. n-1] of search keys and an array freq[0.. n-1] of frequency counts,
where freq[i] is the number of searches to keys[i]. Construct a binary search tree of all keys
such that the total cost of all the searches is as small as possible.
"""


def optimal_bst(keys, freq, level=1):
    if len(keys) == 0:
        return 0
    best_cost = float('inf')
    for i in range(len(keys)):
        left_cost = optimal_bst(keys[:i], freq[:i], level+1)
        right_cost = optimal_bst(keys[i+1:], freq[i+1:], level+1)
        best_cost = min(best_cost, left_cost + right_cost + level*freq[i])
    return best_cost


def optimal_bst_bottom_up(keys, freq):
    n = len(keys)
    # cost[i][j] stores the optimal cost BST by using keys[i...j]
    # The final result is stored in cost[0][n-1]
    cost = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]

    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i+L-1
            rest_cost = sum(freq[i:j + 1])
            # k denotes the root node for the range i...j
            for k in range(i, j+1):
                if k > i:
                    left_cost = cost[i][k-1]
                else:
                    left_cost = 0
                if k < j:
                    right_cost = cost[k+1][j]
                else:
                    right_cost = 0
                cost[i][j] = min(cost[i][j], left_cost + right_cost + rest_cost)

    return cost[0][n-1]


class TestOptimalBST(unittest.TestCase):

    def test_optimal_bst(self):
        keys = [10, 12, 20]
        freq = [34, 8, 50]
        self.assertEqual(optimal_bst_bottom_up(keys, freq), 142)
