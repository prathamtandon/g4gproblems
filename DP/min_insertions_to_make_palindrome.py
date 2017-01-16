import unittest
"""
Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
Input: ab
Output: 1 (bab)
Input: aa
Output: 0
Input: abcd
Output: 3 (dcbabcd)
Input: abcda
Output: 2 (adcbcda) which is same as insertions for bcd.
"""


"""
Approach 1:
1. Let min_insertions(str, start, end) denote the minimum insertions for str[start...end]
2. This problem has the following optimal substructure:
    if str[start]==str[end]:
        min_insertion(str,start,end) = min_insertions(str,start+1,end-1)
    else:
        min_insertion(str,start,end) = 1+min(min_insertions(str,start,end-1),min_insertions(str,start+1,end))
Approach 2:
1. Find the length of LCS between str and reverse(str).
2. Min insertions = N - length of LCS where N is number of characters in str.
"""


def min_insertions_to_make_palindrome(string):

    n = len(string)
    # table[i][j] denotes minimum insertions to make str[i...j] a palindrome.
    # Final result is in table[0][n-1]
    table = [[0] * n for _ in range(n)]

    for L in range(2, n+1):
        for i in range(n-L+1):
            j = i+L-1
            if string[i] != string[j]:
                if L == 2:
                    table[i][j] = 1
                else:
                    table[i][j] = 1 + min(table[i+1][j], table[i][j-1])
            elif L > 2:
                table[i][j] = table[i+1][j-1]

    return table[0][n-1]


class TestMinInsertions(unittest.TestCase):

    def test_min_insertions(self):
        string = 'geeks'
        self.assertEqual(min_insertions_to_make_palindrome(string), 3)
        string = 'abcde'
        self.assertEqual(min_insertions_to_make_palindrome(string), 4)

