import unittest
"""
Given an input string and a dictionary of words, find out if the input string
can be segmented into a space-separated sequence of dictionary words.
Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
  cream, icecream, man, go, mango}
Input:  ilike
Output: Yes
The string can be segmented as "i like".
Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung" or "i like sam sung".
"""

"""
Approach:
1. The problem has the following optimal substructure:
    word_break(string, valid_words):
        n = len(string)
        for i in range(n):
            if string[:i] in valid_words:
                return word_break(string[i+1:], valid_words)
        return False

"""


def word_break(string, valid_words):

    n = len(string)
    # table[i] is True if string[0...i] can be broken into sequence of dictionary words.
    # table[n-1] will store the final result.
    table = [False] * n

    for i in range(n):
        if not table[i] and string[:i+1] in valid_words:
            table[i] = True
        if table[i]:
            for j in range(i+1, n):
                if string[i+1:j+1] in valid_words:
                    table[j] = True
    return table[n-1]


class TestWordBreak(unittest.TestCase):

    def test_word_break(self):
        valid_words = ["mobile", "samsung", "sam", "sung", "man", "mango",
                       "icecream", "and", "go", "i", "like", "ice", "cream"]
        string = 'samsungandmangok'
        self.assertFalse(word_break(string, valid_words))
        string = 'ilikesamsung'
        self.assertTrue(word_break(string, valid_words))
        string = 'iiiiiiii'
        self.assertTrue(word_break(string, valid_words))
        string = 'ilikelikeimangoiii'
        self.assertTrue(word_break(string, valid_words))
        string = 'samsungandmango'
        self.assertTrue(word_break(string, valid_words))
