import unittest
"""
Given an unsorted array, trim the array such that twice of minimum is greater than
maximum in the trimmed array. Elements should be removed only from either ends of the array.
Number of removals should be minimum.
Input: 4 5 100 9 10 11 12 15 200
Output: 4
We need to remove 4, 5, 100 and 200.
Input: 4 7 5 6
Output: 0
We do not need to remove any element.
"""


# Time complexity: O(n^3)
def min_removals(arr):

    n = len(arr)
    # table[i][j] stores minimum removals from arr[i...j] such that 2*min > max
    # table[0][n-1] stores the final result.
    table = [[0] * n for _ in range(n)]

    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i+L-1
            min_ele = min(arr[i:j+1])
            max_ele = max(arr[i:j+1])
            if min_ele * 2 <= max_ele:
                table[i][j] = 1 + min(table[i+1][j], table[i][j-1])

    return table[0][n-1]


# Time complexity: O(n^2)
def min_removals_2(arr):
    # The idea is to consider all subarrays of the given array
    # and find the one which satisfies 2*min > max and has the longest length.
    longest_start = -1
    longest_end = -1
    n = len(arr)
    for start in range(n):
        min_ele = float('inf')
        max_ele = -float('inf')
        for end in range(start, n):
            val = arr[end]
            max_ele = max(val, max_ele)
            min_ele = min(val, min_ele)
            if 2*min_ele <= max_ele:
                break
        if end-start > longest_end-longest_start or longest_start == -1:
            longest_start = start
            longest_end = end

    if longest_start == -1:
        return n-1
    return n-(longest_end-longest_start)-1


class TestMinRemovals(unittest.TestCase):

    def test_min_removals(self):
        arr = [4, 5, 100, 9, 10, 11, 12, 15, 200]
        self.assertEqual(min_removals(arr), 4)
        arr = [4, 7, 5, 6]
        self.assertEqual(min_removals(arr), 0)
        arr = [20, 7, 5, 6]
        self.assertEqual(min_removals(arr), 1)
        arr = [20, 4, 1, 3]
        self.assertEqual(min_removals(arr), 3)
