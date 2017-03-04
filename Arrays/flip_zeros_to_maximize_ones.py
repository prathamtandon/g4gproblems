import unittest
"""
Given a binary array and an integer m, find the position of zeros flipping which creates the maximum
number of consecutive 1s in the array such that number of zeros is <= m.
Input: 1 0 0 1 1 0 1 0 1 1 1
Output: 5 7
"""

"""
Approach:
1. First, compute number of consecutive zeros to the left and right of each zero.
2. Next, for every consecutive m zeros, compute the number of consecutive 1s that can be obtained.
3. Time complexity is O(n) and Space complexity is O(n).
"""

"""
Approach 2:
1. Use a sliding window for the given array.
2. Let left end of the window be wL and right end be wR.
3. Let number of zeros inside the window be zeroCount.
4. We maintain the window with at most m zeros inside.
5. The main steps are:
    a. While zeroCount is at most m, expand the window to the right (wR++) and update zeroCount.
    b. While zeroCount exceeds m, shrink the window from left (wL++), update zeroCount.
    c. Update the widest window along the way.
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


def flip_zeros_sliding_window(ones_and_zeros, m):
    window_left = 0
    window_right = 0
    zero_count = 0

    best_window_size = 0
    best_index = 0

    while window_right < len(ones_and_zeros):
        if zero_count <= m:
            if ones_and_zeros[window_right] == 0:
                zero_count += 1
            window_right += 1
        if zero_count > m:
            if ones_and_zeros[window_left] == 0:
                zero_count -= 1
            window_left += 1
        if window_right - window_left > best_window_size:
            best_window_size = window_right - window_left
            best_index = window_left

    result = []
    while len(result) < m:
        if ones_and_zeros[best_index] == 0:
            result.append(best_index)
        best_index += 1
        if best_index >= len(ones_and_zeros):
            break

    return result


class TestFlips(unittest.TestCase):

    def test_flips(self):
        ones_and_zeros = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
        self.assertEqual(flip_zeros_to_maximize_ones(ones_and_zeros, 2), [5, 7])
        ones_and_zeros = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
        self.assertEqual(flip_zeros_to_maximize_ones(ones_and_zeros, 1), [7])
        ones_and_zeros = [0, 0, 0, 1]
        self.assertEqual(flip_zeros_to_maximize_ones(ones_and_zeros, 4), [0, 1, 2])

    def test_flips_sliding_window(self):
        ones_and_zeros = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
        self.assertEqual(flip_zeros_sliding_window(ones_and_zeros, 2), [5, 7])
        ones_and_zeros = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]
        self.assertEqual(flip_zeros_sliding_window(ones_and_zeros, 1), [7])
        ones_and_zeros = [0, 0, 0, 1]
        self.assertEqual(flip_zeros_sliding_window(ones_and_zeros, 4), [0, 1, 2])
