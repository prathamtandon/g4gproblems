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


class TestSumOfSquares(unittest.TestCase):

    def test_sum_of_squares(self):
        self.assertEqual(n_as_sum_of_squares(4), 2)
        self.assertEqual(n_as_sum_of_squares(5), 2)
        self.assertEqual(n_as_sum_of_squares(16), 8)
