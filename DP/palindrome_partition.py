import unittest
"""
Given a string, a palindrome of the string is a palindrome partitioning if every substring of the partition
is a palindrome. Find fewest cuts needed for palindrome partitioning of given string.
Input: ababbbabbababa
Output: 3 (a|babbbab|b|ababa)
"""


class Palindrome:
    def __init__(self):
        self.palindrome_substring = None
        self.cuts = None

    def min_cuts_palindrome_partitioning(self, string):
        self.initialize(string)
        self.fill_palindrome_substrings(string)
        return self.min_cuts(string)

    def initialize(self, string):
        self.palindrome_substring = [[False] * len(string) for _ in range(len(string))]
        self.cuts = [float('inf')] * len(string)

    def fill_palindrome_substrings(self, string):
        self.make_unit_length_palindromes(string)
        self.make_rest_palindromes(string)

    def make_unit_length_palindromes(self, string):
        n = len(string)
        for i in range(n):
            self.palindrome_substring[i][i] = True

    def make_rest_palindromes(self, string):
        n = len(string)
        for length in range(2, n+1):
            for i in range(n-length+1):
                j = i+length-1
                if length == 2 and string[i] == string[j]:
                    self.palindrome_substring[i][j] = True
                else:
                    self.palindrome_substring[i][j] = string[i] == string[j] and \
                                                      self.palindrome_substring[i + 1][j - 1]

    def min_cuts(self, string):
        n = len(string)
        for i in range(n):
            if self.palindrome_substring[0][i]:
                self.cuts[i] = 0
            else:
                for j in range(i):
                    if self.palindrome_substring[j+1][i]:
                        self.cuts[i] = min(self.cuts[i], 1+self.cuts[j])

        return self.cuts[n-1]


class TestPalindrome(unittest.TestCase):

    def test_min_cuts(self):
        string = 'ababbbabbababa'
        palindrome = Palindrome()
        self.assertEqual(palindrome.min_cuts_palindrome_partitioning(string), 3)
