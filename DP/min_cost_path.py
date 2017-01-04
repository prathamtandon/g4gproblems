import unittest
"""
Given a cost matrix and a position (m,n), write a function
that returns cost of minimum cost path to reach (m,n) from (0,0).
"""


def min_cost_path(cost, m, n):
    w = len(cost[0])
    h = len(cost)
    tc = [[float('inf')] * w for _ in range(h)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 and j == 0:
                tc[i][j] = cost[0][0]
            if i-1 >= 0:
                tc[i][j] = min(tc[i][j], cost[i][j] + tc[i-1][j])
            if j-1 >= 0:
                tc[i][j] = min(tc[i][j], cost[i][j] + tc[i][j-1])
            if i-1 >= 0 and j-1 >= 0:
                tc[i][j] = min(tc[i][j], cost[i][j] + tc[i-1][j-1])

    return tc[m][n]


class TestMinCostPath(unittest.TestCase):

    def test_min_cost_path(self):
        cost = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        self.assertEqual(min_cost_path(cost, 2, 2), 8)

