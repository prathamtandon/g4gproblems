import unittest
"""
Given weights and values of n items, put these items in a knapsack of capacity W to
get the maximum total value in the knapsack. In other words, given two integer arrays
val[0...n-1] and weight[0...n-1] and integer W, capacity of knapsack, find out the maximum
value subset of val[] such that sum of weights of this subset is smaller than or equal to W.
You can either pick an item or drop it (0-1 property).
"""

"""
Approach:
Let KS[w][k] denote the maximum value in the knapsack with remaining capacity = w and number of
items to chose from = k. Then,
KS[w][k] = max(KS[w-wt[k]][k-1]+val[k], KS[w][k-1])
"""


def zero_one_knapsack(W, wt, val):
    num_items = len(wt)
    KS = [[0] * (W+1) for _ in range(num_items)]

    for i in range(num_items):
        for j in range(W+1):
            if i == 0 or j == 0:
                KS[i][j] = 0
            else:
                KS[i][j] = KS[i-1][j]
                if wt[i] <= j:
                    KS[i][j] = max(KS[i][j], KS[i-1][j-wt[i]] + val[i])

    return KS[num_items-1][W]


class TestKnapsack(unittest.TestCase):

    def test_knapsack(self):
        val = [60, 100, 120]
        wt = [10, 20, 30]
        W = 50
        self.assertEqual(zero_one_knapsack(W, wt, val), 220)
