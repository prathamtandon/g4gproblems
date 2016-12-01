import unittest
"""
Given an array of positive and negative numbers in random order, rearrange the array elements
so that positive and negative numbers are placed alternatively. If one type of numbers is more
than half, the extra ones appear at end of array.
Input: -1 2 -3 4 5 6 -7 8 9
Output: 9 -7 8 -3 5 -1 2 4 6
"""

"""
Approach:
1. Get all the positive numbers on one side.
2. Get all the negative numbers on other side.
3. Now swap every alternate negative number with next positive number.
"""


def rearrage_positive_and_negative(list_of_numbers):

    # Get all negative numbers before all positive numbers
    i = -1
    for j in range(len(list_of_numbers)):
        if list_of_numbers[j] < 0:
            i += 1
            list_of_numbers[i], list_of_numbers[j] = list_of_numbers[j], list_of_numbers[i]

    pos_index = i + 1
    neg_index = 0

    while pos_index < len(list_of_numbers) and neg_index < pos_index and list_of_numbers[neg_index] < 0:
        list_of_numbers[pos_index], list_of_numbers[neg_index] = list_of_numbers[neg_index],\
                                                                 list_of_numbers[pos_index]
        pos_index += 1
        neg_index += 2

    return list_of_numbers


class TestRearrangement(unittest.TestCase):

    def test_rearrangement(self):
        result = [4, -3, 5, -1, 6, -7, 2, 8, 9]
        self.assertEqual(rearrage_positive_and_negative([-1, 2, -3, 4, 5, 6, -7, 8, 9]), result)
