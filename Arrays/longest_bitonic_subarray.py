import unittest
"""
Given an array A, find the size of longest bitonic subarray A[i...j]
such that A[i] <= A[i+1] <= ... <= A[k] >= A[k+1] >= ... >= A[j-1] >= A[j]
Input: 12 4 78 90 45 23
Output: 5 (4 78 90 45 23)
"""

"""
Approach:
1. This is similar to finding max j-i such that a[j]>a[i]
2. Compute two auxiliary arrays: longest_increasing_ending_at_me and longest_decreasing_starting_from_me
3. Names should be self-explanatory.
4. Once we have these arrays, return the max among (longest_inc[i] + longest_dec[i] - 1) for all i.
"""


def find_longest_bitonic_array(list_of_numbers):
    longest_increasing_ending_at_me = [1] * len(list_of_numbers)
    longest_decreasing_starting_at_me = [1] * len(list_of_numbers)

    for i in range(1, len(list_of_numbers)):
        if list_of_numbers[i] >= list_of_numbers[i-1]:
            longest_increasing_ending_at_me[i] = longest_increasing_ending_at_me[i-1] + 1

    for i in reversed(range(len(list_of_numbers) - 1)):
        if list_of_numbers[i] >= list_of_numbers[i+1]:
            longest_decreasing_starting_at_me[i] = longest_decreasing_starting_at_me[i+1] + 1

    max_bitonic_size = 0
    for i in range(len(list_of_numbers)):
        max_bitonic_size = max(max_bitonic_size,
                               longest_increasing_ending_at_me[i] + longest_decreasing_starting_at_me[i])

    return max_bitonic_size - 1  # since k gets counted twice


class TestLongestBitonic(unittest.TestCase):

    def test_longest_bitonic(self):
        list_of_numbers = [12, 4, 78, 90, 45, 23]
        self.assertEqual(find_longest_bitonic_array(list_of_numbers), 5)
        list_of_numbers = [20, 4, 1, 2, 3, 4, 2, 10]
        self.assertEqual(find_longest_bitonic_array(list_of_numbers), 5)
        list_of_numbers = [10, 20, 30, 40]
        self.assertEqual(find_longest_bitonic_array(list_of_numbers), 4)
        reversed(list_of_numbers)
        self.assertEqual(find_longest_bitonic_array(list_of_numbers), 4)
        list_of_numbers = [10]
        self.assertEqual(find_longest_bitonic_array(list_of_numbers), 1)
