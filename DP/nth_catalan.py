import unittest
"""
Nth Catalan number is defined as:
C(n) = sum(C(i)*C(n-1-i) for i in range(n))
C[0] = 1
It appears in various applications like:
1. Number of expressions with n pairs of balanced parentheses = C(n)
2. Number of BSTs with n keys = C(n)
3. Number of full binary trees (each node has 0 or 2 child nodes) with n+1 leaves = C(n)

Nth catalan can also be calculated using the following Binomial Coefficient:
Catalan(n) = 1/(n+1) * C(2n, n) where C(n, r) is n choose r.
"""


def nth_catalan(n):

    if n <= 1:
        return 1
    # table[i] stores the ith catalan number
    table = [0] * (n+1)
    table[0] = 1
    table[1] = 1

    for i in range(2, n+1):
        for j in range(i):
            table[i] += table[j] * table[i-j-1]

    return table[n]


class TestCatalan(unittest.TestCase):

    def test_catalan(self):
        self.assertEqual(nth_catalan(4), 14)
        self.assertEqual(nth_catalan(5), 42)
        self.assertEqual(nth_catalan(9), 4862)
