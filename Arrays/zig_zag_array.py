import unittest
"""
Given an array of distinct integers, rearrange elements of array in zig-zag fashion. The converted
array should be in the form: a < b > c < d > e.
Input: 4 3 7 8 6 2 1
Output: 3 7 4 8 2 6 1
Input: 1 4 3 2
Output: 1 4 2 3
"""

"""
Approach:
1. A simple approach is to sort the array in increasing order and swap alternate elements starting second element.
2. Runtime is O(nlogn)
3. A better way is to scan the array from left to right while maintaining the current comparision operator.
4. If current pair is out of place, we swap. Else we flip the comparision operator and move to next pair.
"""


def zig_zag_array(list_of_numbers):
    is_less_than = True
    for i in range(len(list_of_numbers) - 1):
        if is_less_than:
            if list_of_numbers[i] > list_of_numbers[i+1]:
                list_of_numbers[i], list_of_numbers[i+1] = list_of_numbers[i+1], list_of_numbers[i]
        else:
            if list_of_numbers[i] < list_of_numbers[i+1]:
                list_of_numbers[i], list_of_numbers[i + 1] = list_of_numbers[i + 1], list_of_numbers[i]
        is_less_than = not is_less_than


class TestZigZag(unittest.TestCase):

    def test_zig_zag(self):
        list_of_numbers = [4, 3, 7, 8, 6, 2, 1]
        zig_zag_array(list_of_numbers)
        self.assertEqual(list_of_numbers, [3, 7, 4, 8, 2, 6, 1])


