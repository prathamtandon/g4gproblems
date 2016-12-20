import unittest
"""
Given a binary array and an integer m, find the position of zeros flipping which creates the maximum
number of consecutive 1s in the array.
Input: 1 0 0 1 1 0 1 0 1 1 1
Output: 5 7
"""

"""
Approach:
1. First, compute number of consecutive zeros to the left and right of each zero.
2. Next, for every consecutive m zeros, compute the number of consecutive 1s that can be obtained.
3. Time complexity is O(n) and Space complexity is O(n).
"""


def flip_zeros_to_maximize_ones(ones_and_zeros, m):

    consecutive_1s_to_left = [0] * len(ones_and_zeros)
    consecutive_1s_to_right = [0] * len(ones_and_zeros)
    one_count = 0
    end = len(ones_and_zeros)

    for i in range(end):
        if ones_and_zeros[i] == 1:
            one_count += 1
        else:
            consecutive_1s_to_left[i] = one_count
            one_count = 0

    one_count = 0
    for i in range(end-1, -1, -1):
        if ones_and_zeros[i] == 1:
            one_count += 1
        else:
            consecutive_1s_to_right[i] = one_count
            one_count = 0

    zeros = [i for i in range(end) if ones_and_zeros[i] == 0]

    if len(zeros) <= m:
        return zeros

    max_length = 0
    max_index = 0

    for i in range(len(zeros)-m+1):
        cur_length = 0
        remaining_flips = m

        idx = i
        while remaining_flips > 0:
            cur_length += consecutive_1s_to_left[zeros[idx]]
            cur_length += consecutive_1s_to_right[zeros[idx]]
            idx += 1
            remaining_flips -= 1

        if cur_length > max_length:
            max_length = cur_length
            max_index = i

    return zeros[max_index:max_index+m]


class TestFlips(unittest.TestCase):

    def test_flips(self):
        ones_and_zeros = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
        self.assertEqual(flip_zeros_to_maximize_ones(ones_and_zeros, 2), [5, 7])
        ones_and_zeros = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
        self.assertEqual(flip_zeros_to_maximize_ones(ones_and_zeros, 1), [7])
        ones_and_zeros = [0, 0, 0, 1]
        self.assertEqual(flip_zeros_to_maximize_ones(ones_and_zeros, 4), [0, 1, 2])
