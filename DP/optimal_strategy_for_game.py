import unittest
"""
Consider a row of n coins of values v1 ,..., vn, where n is even. We play a game
against an opponent by alternating turns. In each turn, a player selects either the
first or last coin from the row, removes it from the row permanently, and receives the value
of the coin. Determine the maximum possible amount of money with which we can definitely
win if we move first.
"""

"""
Approach:
1. Lets say we have coins[i...j].
2. If we chose coins[i], then opponent will chose maximum amongst coins[i+1] and coins[j].
3. If we chose coins[j], then opponent will chose maximum amongst coins[i] and coins[j-1].
4. Therefore we have following optimal substructure:
    game(coins,i,j) = max(coins[i] + game(coins,i+2,j) if coins[i+1]>coins[j] else game(coins,i+1,j-1),
                          coins[j] + game(coins,i+1,j-2) if coins[i]>coins[j-1] else game(coins,i,j-2))
"""


def optimal_strategy(coins):

    n = len(coins)
    # table[i][j] denotes the maximum value obtained by the player for coins[i...j]
    # table[0][n-1] stores the final result.
    table = [[0] * n for _ in range(n)]

    for i in range(n):
        table[i][i] = coins[i]

    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i+L-1
            if L == 2:
                table[i][j] = max(coins[i], coins[j])
            else:
                x = coins[i]
                if i+2 < n and j-1 >= 0:
                    if coins[i+1] > coins[j]:
                        x += table[i+2][j]
                    else:
                        x += table[i+1][j-1]
                y = coins[j]
                if i+1 < n and j-2 >= 0:
                    if coins[i] > coins[j-1]:
                        y += table[i+1][j-1]
                    else:
                        y += table[i][j-2]
                table[i][j] = max(x, y)

    return table[0][n-1]


class TestOptimalStrategy(unittest.TestCase):

    def test_optimal_strategy(self):
        coins = [5, 3, 7, 10]
        self.assertEqual(optimal_strategy(coins), 15)
        coins = [8, 15, 3, 7]
        self.assertEqual(optimal_strategy(coins), 22)
        coins = [2, 2, 2, 2]
        self.assertEqual(optimal_strategy(coins), 4)
        coins = [20, 30, 2, 2, 2, 10]
        self.assertEqual(optimal_strategy(coins), 42)
