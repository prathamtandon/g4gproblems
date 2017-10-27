import unittest
"""
You are given n pairs of numbers. In every pair first number is always smaller than second number.
A pair (c,d) can follow another pair (a,b) if b < c.
Chain of pairs can be formed in this fashion.
Find the longest chain which can be formed from a given set of pairs.
Input: (5,24),(39,60),(15,28),(27,40),(50,90)
Output: 3, chain is (5,24),(27,40),(50,90)
"""


def chain_of_pairs(pairs):
    pairs = sorted(pairs, cmp=pair_comparator)
    # This is similar to finding LIS where sequence is given pairs.
    n = len(pairs)
    # table[i] denotes length of LIS ending in pairs[i].
    table = [1] * n
    for i in range(1, n):
        for j in range(i):
            if pairs[i][0] > pairs[j][1] and table[i] < table[j] + 1:
                table[i] = table[j] + 1

    return max(table)


def pair_comparator(pair1, pair2):
    return pair1[0] - pair2[0]


class TestChainOfPairs(unittest.TestCase):

    def test_chain_of_pairs(self):
        pairs = [[5, 24], [39, 60], [15, 28], [27, 40], [50, 90]]
        self.assertEqual(chain_of_pairs(pairs), 3)
