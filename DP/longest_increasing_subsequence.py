import unittest


def longest_increasing_subsequence(seq):
    end = len(seq)
    aux = [0]*end

    for i in range(end):
        floor_val = None
        floor_index = -1
        for j in range(i):
            if (floor_val is None and seq[j] < seq[i]) or (floor_val < seq[j] < seq[i]):
                floor_val = seq[j]
                floor_index = j
        if floor_val is None:
            aux[i] = 1
        else:
            aux[i] = aux[floor_index] + 1

    return max(aux)


class TestLIS(unittest.TestCase):

    def test_LIS(self):
        seq = [10, 22, 9, 33, 21, 50, 41, 60, 80]
        self.assertEqual(longest_increasing_subsequence(seq), 6)
