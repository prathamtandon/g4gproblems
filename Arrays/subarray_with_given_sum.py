import unittest
"""
Given an unsorted array of positive integers, find a contiguous subarray
which adds to a given number.
Input: 1 4 20 3 10 5, sum = 33
Output: Sum between indices 2 and 4.
Input: 1 4, sum = 0
Output: No subarray
"""

"""
Approach:
1. Have two pointers, start and end.
2. Keep moving end forward, and keep a running sum.
3. When sum > desired sum, move start forward and keep removing from sum until sum becomes less than sum.
4. Return start and end when running sum becomes equal to desired sum.
"""


def find_subarray_with_given_sum(list_of_numbers, sum):
    running_sum = list_of_numbers[0]
    start = 0

    for end in range(1, len(list_of_numbers)):
        while start < end-1 and running_sum > sum:
            running_sum -= list_of_numbers[start]
            start += 1
        if running_sum == sum:
            return start, end-1
        if end < len(list_of_numbers):
            running_sum += list_of_numbers[end]
    return None


class TestSubarraySum(unittest.TestCase):

    def test_subarray_with_given_sum(self):
        list_of_numbers = [1, 4, 20, 3, 10, 5]
        self.assertEqual(find_subarray_with_given_sum(list_of_numbers, 33), (2, 4))
        list_of_numbers = [15, 2, 4, 8, 9, 5, 10, 23]
        self.assertEqual(find_subarray_with_given_sum(list_of_numbers, 23), (1, 4))
        list_of_numbers = [1, 4]
        self.assertIsNone(find_subarray_with_given_sum(list_of_numbers, 0))
