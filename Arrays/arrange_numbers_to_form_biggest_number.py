import unittest
"""
Given an array of numbers, arrange them in a way that yields the maximum value.
Input: 54 546 548 60
Output: 6054854654
Input: 1 34 3 98 9 76 45 4
Output: 998764543431
"""

"""
Approach:
1. Sort the numbers using a custom comparator.
2. The comparator works as follows: suppose it takes two numbers X and Y.
3. If XY > YX, it returns 1, elif XY < YX, it returns -1 else it returns 0.
4. For eg. suppose X = 60 and Y = 548. XY = 60548, YX = 54860. So, X should come before Y, hence return 1.
"""


def combined_number_compartor(first, second):
    str_first_second = str(first) + str(second)
    str_second_first = str(second) + str(first)
    int_first_second = int(str_first_second)
    int_second_first = int(str_second_first)

    # Sorting is in non-increasing order
    if int_first_second > int_second_first:
        return -1
    elif int_first_second < int_second_first:
        return 1
    return 0


def arrange_numbers_to_form_biggest_number(list_of_numbers):
    list_of_numbers = sorted(list_of_numbers, cmp=combined_number_compartor)
    return int(''.join(map(lambda x: str(x), list_of_numbers)))


class TestArrangement(unittest.TestCase):

    def test_arrangement(self):
        self.assertEqual(arrange_numbers_to_form_biggest_number([54, 546, 548, 60]), 6054854654)


