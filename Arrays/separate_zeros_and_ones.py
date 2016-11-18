import unittest

"""
Given an array of 0s and 1s in random order, segregate 0s and 1s such that all 1s are at the right.
Input: 0 1 0 1 0 0 1 1 1 0
Output: 0 0 0 0 0 1 1 1 1 1
"""

"""
Approach:
1. Have two pointers at the end of array.
2. Decrement till there are zeros
3. When there is a one, swap with rightmost zero
"""


def separate_zeros_and_ones(list_of_zeros_and_ones):
    length = len(list_of_zeros_and_ones)
    left_most_one = length - 1
    right_most_one = length - 1

    while left_most_one >= 0:
        while list_of_zeros_and_ones[left_most_one] == 0:
            left_most_one -= 1
        if left_most_one >= 0:
            temp = list_of_zeros_and_ones[right_most_one]
            list_of_zeros_and_ones[right_most_one] = list_of_zeros_and_ones[left_most_one]
            list_of_zeros_and_ones[left_most_one] = temp
            right_most_one -= 1
            left_most_one -= 1


class TestSegregate(unittest.TestCase):

    def test_separate_zeros_and_ones(self):
        list_of_zeros_and_ones = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
        separate_zeros_and_ones(list_of_zeros_and_ones)
        self.assertEqual(list_of_zeros_and_ones, [0, 0, 0, 0, 0, 1, 1, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()
