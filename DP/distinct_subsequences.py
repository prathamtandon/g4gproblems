import unittest
"""
Given two sequences A and B, find out number of distinct subsequences in A which are equal to B.
Input: A: rabbbit, B: rabbit
Output: 3 [One subsequence which includes first b and one excludes first b]
"""

"""
Approach:
1. Following optimal substructure exists:
 If A[i] != B[j]:
    distinct(A,B,i,j) = distinct(A,B,i-1,j)
 else:
    distinct(A,B,i,j) = distinct(A,B,i-1,j-1) + distinct(A,B,i-1,j)
That is, even when characters match, we may include the match or exlclude the match while looking for subsequence.
"""


def distinct_subsequences(A, B, n, m, table={}):
    if m == 0:
        return 1
    if n == 0:
        return 0
    key = A[:n] + B[:m]
    if key in table:
        return table[key]
    if A[n-1] == B[m-1]:
        result = distinct_subsequences(A, B, n - 1, m - 1) + distinct_subsequences(A, B, n - 1, m)
    else:
        result = distinct_subsequences(A, B, n - 1, m)
    table[key] = result
    return result


class TestDistinctSubsequences(unittest.TestCase):

    def test_distinct_subsequences(self):
        A = 'rabbbit'
        B = 'rabbit'
        self.assertEqual(distinct_subsequences(A, B, len(A), len(B)), 3)
        A = 'geeksforgeeks'
        B = 'ge'
        self.assertEqual(distinct_subsequences(A, B, len(A), len(B)), 6)
        A = 'uwnny'
        B = 'uwnny'
        self.assertEqual(distinct_subsequences(A, B, len(A), len(B)), 1)
