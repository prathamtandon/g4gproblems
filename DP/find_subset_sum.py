import unittest
"""
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set
with sum equal to given sum.
Input: set: 3 34 4 12 5 2, sum: 9
Output: True (3,4,2) or (4,5)
"""

"""
Approach:
1. Let isSubsetSum(set, n, sum) denote if there is a subset within set of n elements with sum = sum.
2. We can either include the last element in the subset or exclude it from the the subset.
3. This leads to below recursion: isSubsetSum(set, n, sum) = isSubsetSum(set, n-1, sum-set[n]) ||
    isSubsetSum(set, n-1, sum)
4. This naive implementation has exponential runtime.
5. Let table[i][j] denote whether there is a subset with sum = i in set[0...j]. The final result is stored in
   table[sum][n].
"""


def subset_sum(arr, sum):
    n = len(arr)
    table = [[False] * (n+1) for _ in range(sum+1)]

    for i in range(n+1):
        table[0][i] = True

    for i in range(1, sum+1):
        for j in range(1, n+1):
            table[i][j] = table[i][j-1]
            if i-arr[j-1] >= 0:
                table[i][j] = table[i-arr[j-1]][j-1] or table[i][j]

    return table[sum][n]


class TestSubsetSum(unittest.TestCase):

    def test_subset_sum(self):
        arr = [3, 34, 4, 12, 5, 2]
        sum = 9
        self.assertTrue(subset_sum(arr, sum))
        sum = 10000
        self.assertFalse(subset_sum(arr, sum))
