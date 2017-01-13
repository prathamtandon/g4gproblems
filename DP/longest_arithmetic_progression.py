import unittest
"""
Given a set of numbers, find the length of longest arithmetic progression.
Input: 1 7 10 15 27 29
Output: 3
Input: 5 10 15 20 25 30
Output: 6
"""

"""
table[i] is a list of 2-tuples. First item in tuple is common difference and second item is
length of AP ending in arr[i]. If current element - arr[i] == tuple[0] for some tuple in table[i],
we add (tuple[0],tuple[1]+1) to table[current element]. Whenever the length changes, we compare
with max length found so far.
"""


def longest_arithmetic_progression_simple(arr):

    n = len(arr)
    table = [[] for _ in range(n)]
    table[0] = [[None, 0]]
    max_so_far = 1
    for i in range(1, n):
        for j in range(i):
            progressions = table[j]
            for progression in progressions:
                common_difference = progression[0]
                if common_difference is not None and arr[i] - arr[j] == common_difference:
                    table[i].append([common_difference, progression[1] + 1])
                    if progression[1] + 1 > max_so_far:
                        max_so_far = progression[1] + 1
                else:
                    table[i].append([arr[i] - arr[j], 2])

    return max_so_far


def longest_arithmetic_progression(arr):

    n = len(arr)
    # table[i][j] stores the length of longest AP having arr[i] and arr[j] as the first two elements.
    # The final result is the maximum value stored in table.
    # The idea is to find three elements in AP in a sorted set.
    # Start from second element and consider each element as middle element of AP.
    # a-d, a, a+d
    # For this to happen for arr[j] we find arr[i] and arr[k] such that:
    # arr[i] + arr[k] = 2*arr[j]
    # This can be done in linear time in a sorted list.
    # Extend the idea for LLAP by:
    # table[i][j] = table[j][k] + 1
    # if we find arr[i], arr[j] and arr[k] are in AP.

    # The minimum longest AP is of length 2. (Any pair of i,j where j>i).
    table = [[2] * (n+1) for _ in range(n+1)]
    max_so_far = 2

    for j in range(n-2, -1, -1):
        i = j-1
        k = j+1
        while i >= 0 and k < n:
            if arr[i] + arr[k] < 2*arr[j]:
                k += 1
            elif arr[i] + arr[k] > 2*arr[j]:
                i -= 1
            else:
                table[i][j] = table[j][k] + 1
                max_so_far = max(max_so_far, table[i][j])
                i -= 1
                k += 1

    return max_so_far


class TestLongestAP(unittest.TestCase):

    def test_longest_ap(self):
        arr = [1, 7, 10, 15, 27, 29]
        self.assertEqual(longest_arithmetic_progression(arr), 3)
        arr = [5, 10, 15, 20, 25, 30]
        self.assertEqual(longest_arithmetic_progression(arr), 6)
        arr = [1, 7, 10, 13, 14, 19]
        self.assertEqual(longest_arithmetic_progression(arr), 4)


