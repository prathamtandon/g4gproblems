import unittest
"""
Write a function that takes two parameters n and k and returns the value of Binomial Coefficient
C(n,k).
Input:
n=4,k=2
Output: 6
1. C(n,k) is the coefficient of X^k in the expansion (1+X)^n
2. C(n,k) is number of k-element subsets of n-element set.
"""

"""
Approach:
C(i,j) = C(i-1,j-1) + C(i-1,j)
This can be interpreted as : We can chose j items from i items by either including the ith item,
in which case we have both one less item to chose from and one less item to chose, OR by excluding
the ith item, in which case we have one less item to chose from but still have j items to chose.
"""


def binomial_coefficent(n, k):
    C = [[0] * (k+1) for _ in range(n+1)]

    for i in range(n+1):
        C[i][0] = 1

    for i in range(k+1):
        C[i][i] = 1

    for i in range(n+1):
        for j in range(k+1):
            if j <= i:
                C[i][j] = C[i-1][j-1] + C[i-1][j]

    return C[n][k]


class TestBinCoefficient(unittest.TestCase):

    def test_bin_coefficient(self):
        self.assertEqual(binomial_coefficent(4, 2), 6)
