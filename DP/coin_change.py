import unittest
"""
Given a value N, if we want to make change for N cents, and we have an infinite supply
of each S = {S1, S2, ..., Sm} valued coins, how many ways can we make the change?
Input: N = 4, S = {1, 2, 3}
Output: {1,1,1,1}, {1,1,2}, {2,2}, {1,3} so total 4 ways.
"""


def coin_change_2(N, S):
    num_denoms = len(S)
    # table[i][j] denotes number of ways to represent sum i using denominations S[0]...S[j]
    # table[N][num_denoms-1] stores the final result.
    table = [[0] * num_denoms for _ in range(N+1)]
    for j in range(num_denoms):
        table[0][j] = 1

    for i in range(1, N+1):
        for j in range(num_denoms):
            # Number of ways to represent i = Number of ways to represent i including S[j] +
            # Number of ways to represent i excluding S[j]
            if i - S[j] >= 0:
                table[i][j] += table[i-S[j]][j]
            if j > 0:
                table[i][j] += table[i][j-1]

    return table[N][num_denoms-1]


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
