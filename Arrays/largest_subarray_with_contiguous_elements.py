import unittest
"""
Given an array of distinct integers, find the length of the longest subarray which contains
numbers that can be arranged in a contiguous sequence.
Input: 10 12 11
Output: 3
Input: 14 12 11 20
Output: 2
Input: 1 56 58 57 90 92 94 93 91 45
Output: 5
"""

"""
Approach:
1. Since all elements are distinct, the largest subarray with contiguous elements will have the following
    property: Difference between min and max in the subarray will be equal to last index - first index in subarray.
2. We scan from left to right, consider all subarrays starting at current index.
3. Time complexity is O(n^2).
"""


def longest_subarray_length_with_contiguous_numbers(list_of_numbers):

    max_subarray_len = -float('inf')
    end = len(list_of_numbers)

    for i in range(end-1):
        cur_min = list_of_numbers[i]
        cur_max = list_of_numbers[i]

        for j in range(i+1, end):
            cur_min = min([cur_min, list_of_numbers[j]])
            cur_max = max([cur_max, list_of_numbers[j]])
            if cur_max-cur_min == j-i:
                max_subarray_len = max([max_subarray_len, j-i+1])

    return max_subarray_len


class TestLongestSubarrayWithContiguousElements(unittest.TestCase):

    def test_longest_subarray(self):
        list_of_numbers = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
        self.assertEqual(longest_subarray_length_with_contiguous_numbers(list_of_numbers), 5)
        list_of_numbers = [10, 12, 11]
        self.assertEqual(longest_subarray_length_with_contiguous_numbers(list_of_numbers), 3)
        list_of_numbers = [14, 12, 11, 20]
        self.assertEqual(longest_subarray_length_with_contiguous_numbers(list_of_numbers), 2)
