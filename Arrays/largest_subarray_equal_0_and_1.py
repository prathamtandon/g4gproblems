import unittest
"""
Given an array containing only 0s and 1s, find the largest subarray which contain equal
number of 0s and 1s.
Input: 1 0 1 1 1 0 0
Output: 1 to 6
Input: 1 1 1 1
Output: No subarray
Input: 0 0 1 1 0
Output: 0 to 3 OR 1 to 4
"""

"""
Approach:
1. Scan the array from left to right.
2. For each index i, compute the difference between count of 1s and 0s to its left, inclusive.
3. A subarray with same number of 0s and 1s will have the same diff value before subarray and after
   subarray, (as net difference within the subarray is zero).
4. We have to find two diff values which are same and maximum distance apart. This can be done using a symbol table.
5. Return the max distance from symbol table.
"""


def find_max_subarray_equal_0_and_1(list_of_zeros_and_ones):

    difference_list = [0] * (len(list_of_zeros_and_ones) + 1)

    ones_count = 0
    zeros_count = 0
    difference_index = 1

    for number in list_of_zeros_and_ones:
        if number == 1:
            ones_count += 1
        else:
            zeros_count += 1
        difference_list[difference_index] = ones_count - zeros_count
        difference_index += 1

    difference_table = {}
    max_length = -float('inf')
    max_length_indices = None

    for i in range(len(difference_list)):
        difference_val = difference_list[i]
        if difference_val in difference_table:
            pair = difference_table[difference_val]
            pair[1] = i
            if max_length < pair[1] - pair[0]:
                max_length = pair[1] - pair[0]
                max_length_indices = [pair[0], pair[1]-1]
        else:
            difference_table[difference_val] = [i, -1]

    return max_length_indices


class TestLargestSubarray(unittest.TestCase):

    def test_largest_subarray(self):
        list_of_zeros_and_ones = [1, 0, 1, 1, 1, 0, 0]
        self.assertEqual(find_max_subarray_equal_0_and_1(list_of_zeros_and_ones), [1, 6])
        list_of_zeros_and_ones = [1, 0, 1, 0, 0, 0, 0]
        self.assertEqual(find_max_subarray_equal_0_and_1(list_of_zeros_and_ones), [0, 3])
        list_of_zeros_and_ones = [1, 0, 1]
        self.assertEqual(find_max_subarray_equal_0_and_1(list_of_zeros_and_ones), [0, 1])
        list_of_zeros_and_ones = [1, 1, 1, 1]
        self.assertIsNone(find_max_subarray_equal_0_and_1(list_of_zeros_and_ones))
