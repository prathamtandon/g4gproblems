import unittest
"""
Given a list of boolean symbols and operators, return the number of ways
the expression can be parenthesized so that it evaluates to True.
Input: symbols: T F F
       operators: ^ |
Output: 2 [((T^F)|F), (T^(F|F))]
"""


def boolean_parenthesization(symbols, operators):

    n = len(symbols)
    # true[i][j] stores the number of parenthesizations such that symbols[i...j] evaluates to True
    # false[i][j] stores the number of parenthesizations such that symbols[i...j] evaluates to False

    # Some notes:
    # Say left and right are subexpressions, then if current operator is:
    # 1. &
    #    num_ways = left is True * right is True
    # 2. |
    #    num_ways = left is True * right is True + left is True * right is False + left is False * right is True
    # 3. ^
    #    num_ways = left is True * right is False + left is False * right is True

    true = [[0] * n for _ in range(n)]
    false = [[0] * n for _ in range(n)]

    for i in range(n):
        if symbols[i] == 'T':
            true[i][i] = 1
        else:
            false[i][i] = 1

    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i+L-1
            for k in range(i, j):
                total_left = true[i][k] + false[i][k]
                total_right = true[k+1][j] + false[k+1][j]
                if operators[k] == '&':
                    true[i][j] += true[i][k] * true[k+1][j]
                    false[i][j] += total_left * total_right - true[i][k] * true[k+1][j]
                elif operators[k] == '|':
                    false[i][j] += false[i][k] * false[k+1][j]
                    true[i][j] += total_left * total_right - false[i][k] * false[k+1][j]
                elif operators[k] == '^':
                    true[i][j] += true[i][k] * false[k+1][j] + false[i][k] * true[k+1][j]
                    false[i][j] += true[i][k] * true[k+1][j] + false[i][k] * false[k+1][j]

    return true[0][n-1]


class TestBooleanParenthesization(unittest.TestCase):

    def test_boolean(self):
        symbols = 'TTFT'
        operators = '|&^'
        self.assertEqual(boolean_parenthesization(symbols, operators), 4)
