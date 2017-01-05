import unittest
"""
Given a string, find the length of the longest substring without repeating characters.
Input: ABDEFGABEF
Output: 6
"""

"""
Approach:
1. Scan the given string from left to right.
2. For each character, maintain the most recent index where that character was last seen.
3. If a repeated character is found, if its last occurrence is not part of current longest substring,
   do nothing, else start a new longest unique substring one index after the last occurrence.
4. Update the max unique length as needed.
"""


def longest_substring_unique_chars(string):
    cur_len = 0
    last_occurrence = {}
    max_len = -float('inf')
    start = 0

    for i in range(len(string)):
        cur_char = string[i]
        if cur_char not in last_occurrence:
            cur_len += 1
        else:
            lo = last_occurrence[cur_char]
            if start <= lo <= start + cur_len:
                max_len = max(max_len, cur_len)
                start = lo + 1
                cur_len = i - start + 1
            else:
                cur_len += 1
        last_occurrence[cur_char] = i

    max_len = max(max_len, cur_len)
    return max_len


class TestLongestUnique(unittest.TestCase):

    def test_longest_unique(self):
        string = 'ABDEFGABEF'
        self.assertEqual(longest_substring_unique_chars(string), 6)
        string = 'GEEKSFORGEEKS'
        self.assertEqual(longest_substring_unique_chars(string), 7)
        string = 'BBBB'
        self.assertEqual(longest_substring_unique_chars(string), 1)
