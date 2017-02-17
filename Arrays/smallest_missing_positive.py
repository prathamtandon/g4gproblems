import unittest
"""
Given an unsorted array of positive and negative numbers, find the smallest missing
positive number.
Input: 2 3 7 6 8 -1 -10 15
Output: 1
Input: 1 1 0 -1 -2
Output: 2
"""

"""
Approach:
1. Move all the negative elements at the right end.
2. Now, use the elements in positive portion of array as an index into the array and make the sign as negative.
3. Do this for entire positive portion.
4. Scan the array from left to right, return first index with a positive element as the missing number.
"""


def shift_negatives_to_right(list_of_numbers):
    i = -1
    for j in range(len(list_of_numbers)):
        if list_of_numbers[j] > 0:
            i += 1
            list_of_numbers[i], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[i]

    return i


def find_smallest_missing_positive(list_of_numbers):
    last_positive_index = shift_negatives_to_right(list_of_numbers)
    for i in range(last_positive_index + 1):
        element_as_index = abs(list_of_numbers[i])-1
        if element_as_index <= last_positive_index and list_of_numbers[element_as_index] > 0:
            list_of_numbers[element_as_index] = -list_of_numbers[element_as_index]
    for i in range(last_positive_index + 1):
        if list_of_numbers[i] > 0:
            return i+1

    return last_positive_index + 2  # +1 for index and another +1 for missing element


class TestSmallestMissingPositive(unittest.TestCase):

    def test_smallest_missing_positive(self):
        list_of_numbers = [2, 3, 7, 6, 8, -1, -10, 15]
        self.assertEqual(find_smallest_missing_positive(list_of_numbers), 1)
        list_of_numbers = [2, 3, -7, 6, 8, 1, -10, 15]
        self.assertEqual(find_smallest_missing_positive(list_of_numbers), 4)
        list_of_numbers = [1, 1, -1, -2]
        self.assertEqual(find_smallest_missing_positive(list_of_numbers), 2)
        list_of_numbers = [-12, 1, 2, -9, -7, 4, -10, 3, 5]
        self.assertEqual(find_smallest_missing_positive(list_of_numbers), 6)
