import unittest
"""
Given two strings, str and pat, find smallest substring in str containing all characters from pat.
NOTE: Assume str and pat only contain ASCII characters.
Input: str = "geeksforgeeks", pat = "ork"
Output: "ksfor"
"""

"""
Approach:
1. Use a sliding window.
2. Keep a count of each character in pat.
3. Now, scan str from left to right and increment count of current char in str.
4. If that char is present in pat too, then increment number of matches by 1.
5. If number of matches becomes equal to length of pat, we have found a window.
6. Try reducing size of window by removing extra characters from left.
7. Return best possible window size.
"""


def smallest_window(str, pat):
    if len(pat) == 0:
        return ""
    if len(pat) > len(str):
        return None
    pat_count = [0] * 256
    str_count = [0] * 256

    pat_length = len(pat)

    for i in range(pat_length):
        pat_count[ord(pat[i])] += 1

    matches = 0
    w_left = 0
    start = -1
    min_size = float('inf')

    for i in range(len(str)):
        str_count[ord(str[i])] += 1

        if pat_count[ord(str[i])] > 0 and pat_count[ord(str[i])] >= str_count[ord(str[i])]:
            matches += 1

        if matches == pat_length:
            while pat_count[ord(str[w_left])] == 0 or str_count[ord(str[w_left])] > pat_count[ord(str[w_left])]:
                if str_count[ord(str[w_left])] > pat_count[ord(str[w_left])]:
                    str_count[ord(str[w_left])] -= 1
                w_left += 1

            cur_size = i - w_left + 1
            if min_size > cur_size:
                min_size = cur_size
                start = w_left

    if start == -1:
        return None

    return str[start: start + min_size]


class TestSmallestWindow(unittest.TestCase):

    def test_smallest_window(self):
        self.assertEqual(smallest_window("aaaacba", "ab"), "ba")
        self.assertEqual(smallest_window("geeksforgeeks", "ork"), "ksfor")
        self.assertEqual(smallest_window("xyz", "yxz"), "xyz")
        self.assertEqual(smallest_window("xyz", "xyz"), "xyz")
        self.assertEqual(smallest_window("xyz", ""), "")
        self.assertIsNone(smallest_window("xyz", "xyzzzzz"))
        self.assertIsNone(smallest_window("dbaac", "xyz"))



