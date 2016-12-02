import unittest
"""
Given an array of random numbers, push all zeros of given array to end of array.
Time complexity: O(n) and Space complexity: O(1)
Input: 1 9 8 4 0 0 2 7 0 6 0
Output: 1 9 8 4 2 7 6 0 0 0 0
"""

"""
Approach:
1. Scan array from left to right.
2. Keep a variable to count number of non-zero items in the array.
3. If item is non-zero, replace item at index count with current non-zero item. Then increment count.
4. This way, after scanning the array once, all non-zero items will be at left end.
5. Scan the array again from last value of count and set all items to zero till the end.
"""


def move_zeros_to_end(list_of_numbers):

    non_zero_index = 0

    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] != 0:
            list_of_numbers[non_zero_index] = list_of_numbers[i]
            non_zero_index += 1

    for i in range(non_zero_index, len(list_of_numbers)):
        list_of_numbers[i] = 0

    return list_of_numbers


class TestMoveZerosToEnd(unittest.TestCase):

    def test_move_zeros_to_end(self):
        list_of_numbers = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
        self.assertEqual(move_zeros_to_end(list_of_numbers), [1, 9, 8, 4, 2, 7, 6, 0, 0, 0, 0])
