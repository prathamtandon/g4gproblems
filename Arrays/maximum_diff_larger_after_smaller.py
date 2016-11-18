import unittest
"""
Given an array of integers, find out the maximum difference between any two elements,
such that larger element appears after the smaller element.
Input: 2 3 10 6 4 8 1
Output: 8 (10 - 2)
Input: 7 9 5 6 3 2
Ouput: 2 (9 - 7)
"""

"""
Approach:
1. Keep track of two variables: minimum element found so far and maximum difference found so far
2. Scan the array from left to right.
3. Update variables as needed.
4. Return max difference found so far.
"""


def max_difference_larger_after_smaller(list_of_numbers):
    max_diff = -float('inf')
    min_val = float('inf')

    for num in list_of_numbers:
        if num < min_val:
            min_val = num
        elif num - min_val > max_diff:
            max_diff = num - min_val

    return max_diff


class TestMaximumDifference(unittest.TestCase):

    def test_maximum_difference(self):
        list_of_numbers = [2, 3, 10, 6, 4, 8, 1]
        self.assertEqual(max_difference_larger_after_smaller(list_of_numbers), 8)
        list_of_numbers = [7, 9, 5, 6, 3, 2]
        self.assertEqual(max_difference_larger_after_smaller(list_of_numbers), 2)


if __name__ == '__main__':
    unittest.main()
