import unittest
"""
Given two strings 'X' and 'Y', find the length of longest common substring.
Input: 'X': 'GeeksforGeeks', 'Y': 'GeeksQuiz'
Output: 5
Input: 'X': 'abcdxyz', 'Y': 'xyzabcd'
Output: 4
Input: 'X': 'zxabcdezy', 'Y': 'yzabcdezx'
Output: 6
"""


"""
Approach:
1. Longest common suffix is defined as :
    longest_common_suffix(X,Y,m,n) = 1+longest_common_suffix(X,Y,m-1,n-1) if X[m-1]==Y[n-1]
                                     0 otherwise
2. Longest common substring is the length of maximum longest common suffix longest_common_suffix(X,Y,i,j)
   for 1<=i<=m and 1<=j<=n.
"""


def longest_common_substring(string1, string2):

    m = len(string1)
    n = len(string2)

    # table[i][j] stores length of longest common substring ending in string1[i] and string2[j]
    # table[m-1][n-1] will store the final result
    table = [[0] * (n+1) for _ in range(m+1)]
    max_length = -float('inf')

    for i in range(1, m+1):
        for j in range(1, n+1):
            if string1[i-1] == string2[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = 0
            max_length = max(max_length, table[i][j])

    return max_length


class TestLongestCommonSubstring(unittest.TestCase):

    def test_longest_common_substring(self):
        string1 = 'abcdxyz'
        string2 = 'xyzabcd'
        self.assertEqual(longest_common_substring(string1, string2), 4)
        string1 = 'GeeksQuiz'
        string2 = 'GeeksforGeeks'
        self.assertEqual(longest_common_substring(string1, string2), 5)
        string1 = 'OldSite:GeeksforGeeks.org'
        string2 = 'NewSite:GeeksQuiz.com'
        self.assertEqual(longest_common_substring(string1, string2), 10)
