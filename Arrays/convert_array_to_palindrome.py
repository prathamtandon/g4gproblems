import unittest
"""
Given an array of positive integers, we need to make the array a Palindrome.
Only merge operations are allowed. Merging two adjacent elements means replacing the elements
by their sum. A single element array is Palindrome.
Input: 15 4 15
Output: 0
Input: 1 4 5 1
Output: 1 (merging 4 and 5)
Input: 11, 14, 15, 99
Output: 3 (all adjacent elements have to be merged to get a single element at the end).
"""

"""
Approach:
1. Keep two pointers: left and right at each end of the array.
2. If sum at left end is equal to sum at right end, move both pointers in opposite directions.
3. If left sum is smaller, merge leftmost elements.
4. Else merge rightmost elements.
"""


def convert_array_to_palindrome(list_of_numbers):

    left = 0
    right = len(list_of_numbers) - 1
    left_sum = list_of_numbers[left]
    right_sum = list_of_numbers[right]
    num_ops = 0

    while left < right:
        if left_sum == right_sum:
            left += 1
            right -= 1
            left_sum = list_of_numbers[left]
            right_sum = list_of_numbers[right]
        elif left_sum < right_sum:
            left += 1
            left_sum += list_of_numbers[left]
            num_ops += 1
        else:
            right -= 1
            right_sum += list_of_numbers[right]
            num_ops += 1

    return num_ops


class TestConvertToPalindrome(unittest.TestCase):

    def test_convert_to_palindrome(self):
        list_of_numbers = [15, 4, 15]
        self.assertEqual(convert_array_to_palindrome(list_of_numbers), 0)
        list_of_numbers = [1, 4, 5, 1]
        self.assertEqual(convert_array_to_palindrome(list_of_numbers), 1)
        list_of_numbers = [11, 14, 15, 99]
        self.assertEqual(convert_array_to_palindrome(list_of_numbers), 3)
