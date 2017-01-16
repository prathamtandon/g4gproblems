import unittest
"""
Given a string, find the longest substring which is a palindrome.
Input: forgeeksskeegfor
Output: geeksskeeg
"""


def longest_palindromic_substring(string):
    n = len(string)
    # table[i][j] is the length of palindromic substring starting at str[i] and ending at str[j].
    # The max value in the table is the final result.
    table = [[0] * n for _ in range(n)]
    for i in range(n):
        table[i][i] = 1

    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if string[i] == string[j] and l == 2:
                table[i][j] = 2
            elif string[i] == string[j]:
                table[i][j] = 2 + table[i+1][j-1]

    start = 0
    max_length = 0
    for i in range(n):
        for j in range(n):
            if max_length < table[i][j]:
                max_length = table[i][j]
                start = i

    return string[start:start+max_length]


class TestLongestPalindromic(unittest.TestCase):

    def test_longest_palindromic(self):
        string = 'forgeeksskeegfor'
        self.assertEqual(longest_palindromic_substring(string), 'geeksskeeg')
