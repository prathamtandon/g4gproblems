import unittest
"""
Manacher O(N) algorithm to find the longest Palindromic substring.
"""


def manacher(input_str):
    N = len(input_str)
    # Number of center positions
    N = 2 * N + 1
    # LPS array
    L = [0] * N
    L[1] = 1
    # center of current palindromic substring
    center = 1
    # right of current palindromic substring
    center_right = 2

    max_lps_len = 0
    max_lps_pos = 0

    for i in range(2, N):
        # center of smaller palindromic substring to right
        current_right = i
        # center of corresponding palindromic substring to left
        current_left = 2 * center - i
        expand = False
        diff = center_right - current_right
        if diff > 0:
            # Case 1: left palindromic substring is completely contained within central palindrome but not its prefix
            if L[current_left] < diff:
                L[current_right] = L[current_left]
            # Case 2: left palindromic substring is prefix and central palindrome is suffix of original string
            elif L[current_left] == diff and L[center_right] == N-1:
                L[current_right] = L[current_left]
            # Case 3: left palindromic substring is prefix and central palindrome is not suffix
            elif L[current_left] == diff and L[center_right] < N-1:
                expand = True
                L[current_right] = L[current_left]
            # Case 4: left palindromic substring expands beyond left end of central palindrome
            elif L[current_left] > diff:
                expand = True
                L[current_right] = diff
        else:
            expand = True
            L[current_right] = 0

        if expand:
            # We will expand not from current_right but from L[current_right] characters away from current_right
            # center. If it is an even position, we simply increment L[i] by 1. If it is odd position, we
            # increment by 1 if actual string characters at those positions are equal.
            while current_right - L[current_right] > 0 and current_right + L[current_right] < N-1 and \
                    ((current_right - L[current_right] - 1) % 2 == 0 or
                     (input_str[(current_right + L[current_right] + 1) / 2] ==
                      input_str[(current_right - L[current_right] - 1) / 2])):
                L[current_right] += 1

        if L[current_right] > max_lps_len:
            max_lps_pos = current_right
            max_lps_len = L[current_right]

        if current_right + L[current_right] > center_right:
            center = current_right
            center_right = current_right + L[current_right]

    # convert from center based positions to actual string indices
    start = (max_lps_pos - max_lps_len) / 2
    end = start + max_lps_len

    return input_str[start:end]


class TestManacher(unittest.TestCase):

    def test_manacher(self):
        self.assertEqual(manacher('abba'), 'abba')
        self.assertEqual(manacher('babcbabcbaccba'), 'abcbabcba')
        self.assertEqual(manacher('forgeeksskeegfor'), 'geeksskeeg')
        self.assertEqual(manacher('abacdfgdcabba'), 'abba')





