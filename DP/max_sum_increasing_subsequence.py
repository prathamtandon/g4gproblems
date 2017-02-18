import unittest
"""
Given an array of n positive integers, find sum of maximum sum subsequence,
such that integers in subsequence are sorted in increasing order.
Input: 1 101 2 3 100 4 5
Output: 1 2 3 100: 106
"""


def max_sum_increasing_subsequence(arr):
    n = len(arr)
    table = [0] * n
    for i in range(n):
        table[i] = arr[i]

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and table[i] < table[j] + arr[i]:
                table[i] = table[j] + arr[i]

    return max(table)


class TestMaxSumIncreasingSS(unittest.TestCase):

    def test_max_sum_increasing_ss(self):
        arr = [1, 101, 2, 3, 100, 4, 5]
        self.assertEqual(max_sum_increasing_subsequence(arr), 106)
