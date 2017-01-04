import unittest


def longest_common_subsequence(first_seq, second_seq):

    m = len(first_seq)
    n = len(second_seq)

    aux = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                aux[i][j] = 0
            elif first_seq[i-1] == second_seq[j-1]:
                aux[i][j] = aux[i-1][j-1] + 1
            else:
                aux[i][j] = max(aux[i-1][j], aux[i][j-1])

    """
    Extract LCS
    """
    lcs = [''] * aux[m][n]
    i = m
    j = n
    k = len(lcs)-1
    while i > 0 and j > 0:
        if first_seq[i-1] == second_seq[j-1]:
            lcs[k] = first_seq[i-1]
            k -= 1
            i -= 1
            j -= 1
        elif aux[i-1][j] > aux[i][j-1]:
            i -= 1
        else:
            j -= 1

    # print ''.join(lcs)

    return aux[m][n]


class TestLCS(unittest.TestCase):

    def test_lcs(self):
        first_seq = 'AGGTAB'
        second_seq = 'GXTXAYB'

        self.assertEqual(longest_common_subsequence(first_seq, second_seq), 4)
