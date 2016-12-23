import unittest
"""
Given a sorted array of integers, return the number of distinct absolute values
among the elements of the array. The input can contain duplicate values.
Input: -3 -2 0 3 4 5
Output: 5
"""

"""
Approach:
1. Scan using two pointers.
2. Take care of duplicates and same absolute values.
"""


def absolute_distinct_count(sorted_list):

    left = 0
    right = len(sorted_list) - 1
    prev_distinct = None
    count = 0

    while left <= right:
        if prev_distinct is not None and abs(sorted_list[left]) == prev_distinct:
            left += 1
        elif prev_distinct is not None and abs(sorted_list[right]) == prev_distinct:
            right -= 1
        elif abs(sorted_list[left]) == abs(sorted_list[right]):
            prev_distinct = abs(sorted_list[left])
            count += 1
            left += 1
            right -= 1
        elif abs(sorted_list[left]) > abs(sorted_list[right]):
            prev_distinct = abs(sorted_list[left])
            count += 1
            left += 1
        else:
            prev_distinct = abs(sorted_list[right])
            count += 1
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
