import unittest
"""
Given an array, only rotation operation is allowed on array. We can rotate the array as many times as we want.
Return the maximum possible of summation of i*arr[i]
Input: 1 20 2 10
Output: 72 by rotating the array 2 times.
"""


def max_sum_with_rotations(list_of_numbers):
    end = len(list_of_numbers)
    indices = range(end)
    max_sum = sum([list_of_numbers[i] * indices[i] for i in range(end)])

    for rotation in range(end-1):
        indices = [(x+1) % end for x in indices]
        cur_sum = sum([list_of_numbers[i] * indices[i] for i in range(end)])
        max_sum = max(max_sum, cur_sum)

    return max_sum


class TestMaxSumWithRotations(unittest.TestCase):

    def test_max_sum_with_rotations(self):
        list_of_numbers = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(max_sum_with_rotations(list_of_numbers), 330)

