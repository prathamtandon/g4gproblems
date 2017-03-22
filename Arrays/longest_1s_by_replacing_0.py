import unittest
"""
Given an array of 0s and 1s, find the position of 0 to be replaced with 1 to get longest contiguous
sequence of 1s.
Input: 1 1 0 0 1 0 1 1 1 0 1 1 1
Output: index 9
Input: 1 1 1 1 0
Output: index 4
Input: 0 1 0 1 0
Output: index 2
"""

"""
Approach:
1. The idea is to keep track of 2 indexes - prev_zero and prev_prev_zero.
2. If current number is zero, calculate the difference between current index and prev_prev_zero.
3. This difference minus 1 is the number of 1s around prev_zero.
4. Update max_difference so far by comparing with difference from previous step.
5. Return the prev_zero index corresponding to max_difference as the answer.
"""


def index_of_zero_to_get_longest_1s(ones_and_zeros):

    prev_zero = -1
    prev_prev_zero = -1
    end = len(ones_and_zeros)
    max_index = -1
    max_1s_length = 0

    for i in range(end):
        if ones_and_zeros[i] == 0:
            if i-prev_prev_zero > max_1s_length:
                max_1s_length = i-prev_prev_zero
                max_index = prev_zero
            prev_prev_zero = prev_zero
            prev_zero = i

    if end-prev_prev_zero > max_1s_length:
        max_index = prev_zero

    return max_index


class TestMax1s(unittest.TestCase):

    def test_max_1s_length(self):
        ones_and_zeros = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]
        self.assertEqual(index_of_zero_to_get_longest_1s(ones_and_zeros), 9)
        ones_and_zeros = [1, 1, 1, 1, 0]
        self.assertEqual(index_of_zero_to_get_longest_1s(ones_and_zeros), 4)
        ones_and_zeros = [1, 1]
        self.assertEqual(index_of_zero_to_get_longest_1s(ones_and_zeros), -1)
