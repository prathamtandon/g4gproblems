import unittest
"""
Given an array, only rotation operation is allowed on array. We can rotate the array as many times as we want.
Return the maximum possible of summation of i*arr[i]
Input: 1 20 2 10
Output: 72 by rotating the array 2 times.
"""


def max_sum_with_rotations(list_of_numbers):
    S = sum(list_of_numbers)
    n = len(list_of_numbers)
    current = 0

    for i in range(n):
        current += i*list_of_numbers[i]
    max_so_far = current

    for i in range(n-1):
        current = current - S + n*list_of_numbers[i]
        max_so_far = max(max_so_far, current)

    return max_so_far


class TestMaxSumWithRotations(unittest.TestCase):

    def test_max_sum_with_rotations(self):
        list_of_numbers = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(max_sum_with_rotations(list_of_numbers), 330)
        list_of_numbers = [1, 20, 2, 10]
        self.assertEqual(max_sum_with_rotations(list_of_numbers), 72)

