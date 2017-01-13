import unittest
"""
Given a rope of length n meters, cut the rope in different parts of integer lengths to
maximize product of length of all parts.
Input: n = 2
Output: 1*1
Input: n = 3
Output: 1*2
Input: 4
Output: 2*2
Input: 10
Output: 3*4*4
"""

"""
Approach:
Optimal substructure:
max_product(n) = max(i*(n-i), i*max_product(n-i)) for i = 1,2,..,n-1
"""


def max_product_rod_cutting(n):

    assert n >= 2
    table = [-float('inf')] * (n+1)

    table[1] = 1
    table[2] = 1

    for i in range(3, n+1):
        for j in range(2, i):
            table[i] = max(table[i], j*(i-j), j * table[i-j])

    return table[n]


class TestMaxProductRodCutting(unittest.TestCase):

    def test_max_product_rod_cutting(self):
        self.assertEqual(max_product_rod_cutting(10), 36)
        self.assertEqual(max_product_rod_cutting(4), 4)
