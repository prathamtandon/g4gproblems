import unittest
"""
Given three strings A, B and C, write a function that checks whether C is an interleaving of A and B.
C is said to be an interleaving of A and B, if it contains all characters of A and B and order of all
characters in individual strings is preserved.
"""

"""
Approach:
1. Following is the overlapping substructure in this problem:
    interleaving(A, B, C, l, m, n) = ((C[n] == A[l] and interleaving(A, B, C, l-1, m, n-1)) OR
                                      (C[n] == B[m] and interleaving(A, B, C, l, m-1, n-1))
"""


def interleaving(first, second, target):

    m = len(first)
    n = len(second)

    # table[i][j] is True if target[0...i+j-1] is an interleaving of first[0...i] and second[0...j]
    # table[m][n] stores the final result.
    table = [[False] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 and j == 0:
                table[i][j] = True
            elif i == 0 and second[j-1] == target[j-1]:
                table[i][j] = table[i][j-1]
            elif j == 0 and first[i-1] == target[i-1]:
                table[i][j] = table[i-1][j]
            elif first[i-1] == target[i+j-1] and second[j-1] != target[i+j-1]:
                table[i][j] = table[i-1][j]
            elif first[i-1] != target[i+j-1] and second[j-1] == target[i+j-1]:
                table[i][j] = table[i][j-1]
            elif first[i-1] == target[i+j-1] and second[j-1] == target[i+j-1]:
                table[i][j] = table[i][j-1] or table[i-1][j]

    return table[m][n]


class TestInterleaving(unittest.TestCase):

    def test_interleaving(self):
        self.assertFalse(interleaving('XXY', 'XXZ', 'XXZXXXY'))
        self.assertTrue(interleaving('WZ', 'XY', 'XYWZ'))
        self.assertFalse(interleaving('YX', 'X', 'XXY'))
        self.assertTrue(interleaving('XXY', 'XXZ', 'XXXXZY'))
