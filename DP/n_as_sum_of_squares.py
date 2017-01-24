import unittest
from math import sqrt
"""
Find number of ways to represent n as a sum of squares of integers.
For eg:
Input: 4
Output: 2 (1^2+1^2+1^2+1^2, 2^2)

The problem can be converted into coin change problem where available denomination of coins are:
[1^2,2^2,...,sqrt(N)*sqrt(N)]
"""


def n_as_sum_of_squares(n):
    ways = [0] * (n+1)
    ways[0] = 1
    s_list = [x*x for x in range(1, int(sqrt(n))+1)]

    for s in s_list:
        for i in range(s, n+1):
            ways[i] += ways[i-s]

    return ways[n]


def n_as_sum_of_integers(n):
    smaller = [x for x in range(1, n)]
    # table[i][j] stores number of ways to denote i as sum of integers using only smaller[0...j]
    # table[n][len(smaller)-1] stores the final result.
    table = [[0] * len(smaller) for _ in range(n+1)]

    for i in range(len(smaller)):
        table[0][i] = 1

    for i in range(1, n+1):
        for j in range(len(smaller)):
            if i - smaller[j] >= 0:
                table[i][j] += table[i - smaller[j]][j]
            if j > 0:
                table[i][j] += table[i][j-1]

    return table[n][len(smaller)-1]


class TestSumOfSquares(unittest.TestCase):

    def test_sum_of_squares(self):
        self.assertEqual(n_as_sum_of_squares(4), 2)
        self.assertEqual(n_as_sum_of_squares(5), 2)
        self.assertEqual(n_as_sum_of_squares(16), 8)


class TestSumOfInts(unittest.TestCase):

    def test_sum_of_ints(self):
        self.assertEqual(n_as_sum_of_integers(5), 6)
        self.assertEqual(n_as_sum_of_integers(4), 4)
