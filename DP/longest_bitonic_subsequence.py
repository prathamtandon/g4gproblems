import unittest
"""
Given an array arr[0...n-1] containing n positive integers, a subsequence arr[] is called Bitonic
if it is first increasing then decreasing. Write a function that takes an array as argument
and returns the length of the longest bitonic subsequence.
"""


def longest_bitonic_subsequence(arr):
    n = len(arr)
    table1 = [1] * n
    table2 = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and table1[i] < table1[j] + 1:
                table1[i] = table1[j] + 1

    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[i] and table2[i] < table2[j] + 1:
                table2[i] = table2[j] + 1

    res = -float('inf')
    for i in range(n):
        res = max(res, table1[i] + table2[i])
    return res - 1


class TestLongestBitonicSS(unittest.TestCase):

    def test_longest_bitonic_ss(self):
        arr = [1, 11, 2, 10, 4, 5, 2, 1]
        self.assertEqual(longest_bitonic_subsequence(arr), 6)
        arr = [12, 11, 40, 5, 3, 1]
        self.assertEqual(longest_bitonic_subsequence(arr), 5)
