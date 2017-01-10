import unittest
"""
Given n dice with m faces, numbered from 1 to m, find the number of ways to get sum X.
X is summation of values on each face when all the dice are thrown.
"""


def dice_throw(X, n, m):

    # table[i][j] denote number of ways to get sum i using j dices.
    # table[X][n] stores the final result.
    table = [[0] * (n+1) for _ in range(X+1)]

    # table[1...min(m,X)][1] is 1 (using only 1 dice).
    for i in range(1, m+1):
        if i <= X:
            table[i][1] = 1

    for i in range(1, X+1):
        for j in range(1, n+1):
            for p in range(1, m+1):
                if i-p >= 0:
                    table[i][j] += table[i-p][j-1]

    return table[X][n]


class TestDiceThrow(unittest.TestCase):

    def test_dice_throw(self):
        m = 6
        n = 3
        X = 8
        self.assertEqual(dice_throw(X, n, m), 21)

        m = 4
        n = 2
        X = 1
        self.assertEqual(dice_throw(X, n, m), 0)

        m = 4
        n = 2
        X = 5
        self.assertEqual(dice_throw(X, n, m), 4)
