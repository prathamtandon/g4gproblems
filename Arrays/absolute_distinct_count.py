import unittest
"""
Given a sorted array of integers, return the number of distinct absolute values
among the elements of the array. The input can contain duplicate values.
Input: -3 -2 0 3 4 5
Output: 5
"""

"""
Approach:
1. Initialize count as total number of elements in array.
2. There can be two types of duplicates: same value and same sign OR same value and opposite sign.
3. Have two pointers, left and right at the two ends of the array.
4. For handling first type of duplicates, keep moving the pointers till values are same.
5. For handling second type of duplicates, sum of arr[left] and arr[right] will be zero for such a pair.
"""


def absolute_distinct_count(sorted_list):

    left = 0
    right = len(sorted_list) - 1
    count = len(sorted_list)

    while left < right:
        # First type of duplicates:
        while left != right and sorted_list[left] == sorted_list[left + 1]:
            count -= 1
            left += 1
        while left != right and sorted_list[right] == sorted_list[right - 1]:
            count -= 1
            right -= 1

        # break if only one element
        if left == right:
            break

        # Second type of duplicate:
        if sorted_list[left] + sorted_list[right] == 0:
            count -= 1
            left += 1
            right -= 1
        elif sorted_list[left] + sorted_list[right] < 0:
            left += 1
        else:
            right -= 1

    return count


class TestAbsoluteDistinctCounts(unittest.TestCase):

    def test_absolute_distinct_counts(self):
        sorted_list = [-3, -2, 0, 3, 4, 5]
        self.assertEqual(absolute_distinct_count(sorted_list), 5)
        sorted_list = [-1, -1, -1, -1, 0, 1, 1, 1, 1]
        self.assertEqual(absolute_distinct_count(sorted_list), 2)
        sorted_list = [-1, -1, -1, -1, 0]
        self.assertEqual(absolute_distinct_count(sorted_list), 2)
        sorted_list = [0, 0, 0]
        self.assertEqual(absolute_distinct_count(sorted_list), 1)
