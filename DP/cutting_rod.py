import unittest
"""
Given a rod of length n inches, and an array of prices that contains prices of all pieces
of size smaller than n, determine the maximum value obtainable by cutting up the rod and selling
the pieces.
Input: Rod length: 8
Prices: 1 2 3 4  5  6  7  8
        1 5 8 9 10 17 17 20
Output: 22 (By cutting in two pieces of length 2 and 6).
"""


def rod_cutting(N, prices):
    table = [-float('inf')] * (N+1)
    table[0] = 0
    for i in range(1, N+1):
        for j in range(1, i+1):
            table[i] = max(table[i], prices[j] + table[i-j])
    return table[N]


class TestRodCutting(unittest.TestCase):

    def test_rod_cutting(self):
        N = 8
        prices = {
            1: 1,
            2: 5,
            3: 8,
            4: 9,
            5: 10,
            6: 17,
            7: 17,
            8: 20
        }
        self.assertEqual(rod_cutting(N, prices), 22)
