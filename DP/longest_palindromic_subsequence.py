import unittest
"""
Given a sequence, find the length of the longest palindromic subsequence in it.
Input: BBABCBCAB
Output: 7
"""


def longest_palindromic_subsequence(string):

    n = len(string)
    #  table[i][j] is longest palindromic subsequence length for string[i...j]
    table = [[0] * n for _ in range(n)]

    for L in range(1, n+1):
        for i in range(n-L+1):
            j = i+L-1
            if i == j:
                table[i][j] = 1
            elif string[i] == string[j] and L == 2:
                table[i][j] = 2
            elif string[i] == string[j]:
                table[i][j] = 2 + table[i+1][j-1]
            else:
                table[i][j] = max(table[i+1][j], table[i][j-1])

    return table[0][n-1]


class TestLPSS(unittest.TestCase):

    def test_lpss(self):
        string = 'GEEKS'
        self.assertEqual(longest_palindromic_subsequence(string), 2)
        self.assertEqual(longest_palindromic_subsequence('BBABCBCAB'), 7)
