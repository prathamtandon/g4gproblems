import unittest

"""
Given two sorted arrays, one of size n and one of size m+n containing only m elements,
merge the smaller array into the larger array such that output is sorted.
Note: NA means empty slot
Input: larger => 2 NA 7 NA NA 10 NA
       smaller => 5 8 12 14
Output: 2 5 7 8 10 12 14
"""

"""
Approach:
1. Move all (non-NA) elements in larger array to the right.
2. Keep one index at start of smaller array, and one index after n positions in larger array.
3. Keep one index at start of larger array.
4. Compare elements and place the smaller at the start of larger array.
5. Increment indices accordingly.
"""


def move_to_right(list_of_numbers):
    destination = len(list_of_numbers) - 1
    index = len(list_of_numbers) - 1
    while index >= 0:
        if list_of_numbers[index] is not None:
            list_of_numbers[destination] = list_of_numbers[index]
            destination -= 1
        index -= 1


def merge_lists(larger_list, smaller_list):
    smaller_index = 0
    larger_index = len(smaller_list)
    destination = 0

    while smaller_index < len(smaller_list):
        if larger_index < len(larger_list) and larger_list[larger_index] <= smaller_list[smaller_index]:
            larger_list[destination] = larger_list[larger_index]
            larger_index += 1
        else:
            larger_list[destination] = smaller_list[smaller_index]
            smaller_index += 1
        destination += 1


def merge_smaller_into_larger(larger_list, smaller_list):
    move_to_right(larger_list)
    merge_lists(larger_list, smaller_list)


class TestMerge(unittest.TestCase):

    def test_merge_smaller_array_has_largest_element(self):
        smaller_list = [5, 8, 12, 14]
        larger_list = [2, None, 7, None, None, 10, None]

        merge_smaller_into_larger(larger_list, smaller_list)
        self.assertEqual(larger_list, [2, 5, 7, 8, 10, 12, 14])

    def test_merge_larger_array_has_largest_element(self):
        smaller_list = [5, 8, 12, 14]
        larger_list = [9, None, 22, None, None, None]

        merge_smaller_into_larger(larger_list, smaller_list)
        self.assertEqual(larger_list, [5, 8, 9, 12, 14, 22])

    def test_merge_same_elements_in_both_lists(self):
        smaller_list = [5, 12]
        larger_list = [None, 5, 12, None]

        merge_smaller_into_larger(larger_list, smaller_list)
        self.assertEqual(larger_list, [5, 5, 12, 12])
