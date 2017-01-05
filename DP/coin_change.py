import unittest
"""
Given a value N, if we want to make change for N cents, and we have an infinite supply
of each S = {S1, S2, ..., Sm} valued coins, how many ways can we make the change?
Input: N = 4, S = {1, 2, 3}
Output: {1,1,1,1}, {1,1,2}, {2,2}, {1,3} so total 4 ways.
"""


def coin_change(N, S):
    ways = [0]*(N+1)
    ways[0] = 1
    for i in range(len(S)):
        for j in range(S[i], N+1):
            ways[j] += ways[j - S[i]]

    return ways[N]


class TestCoinChange(unittest.TestCase):

    def test_coin_change(self):
        S = [3, 2, 1]
        N = 4
        self.assertEqual(coin_change(N, S), 4)
