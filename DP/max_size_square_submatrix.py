import unittest
"""
Given a binary matrix, find out the maximum size of square sub-matrix with all 1s.
Input:
    0  1  1  0  1
    1  1  0  1  0
    0  1  1  1  0
    1  1  1  1  0
    1  1  1  1  1
    0  0  0  0  0
Output:
    1  1  1
    1  1  1
    1  1  1
"""


def length_of_1s_starting_from_me(bin_matrix):
    for i in range(len(bin_matrix)):
        one_count = 0
        for j in range(len(bin_matrix[0])-1, -1, -1):
            if bin_matrix[i][j] == 0:
                one_count = 0
            else:
                one_count += 1
            bin_matrix[i][j] = one_count


def max_size_square_submatrix(bin_matrix):
    length_of_1s_starting_from_me(bin_matrix)
    max_size = -float('inf')
    for i in range(len(bin_matrix)):
        for j in range(len(bin_matrix[0])):
            if bin_matrix[i][j] > 0:
                side_length = bin_matrix[i][j]
                found = True
                for k in range(1, side_length):
                    if i+k >= len(bin_matrix) or bin_matrix[i+k][j] < side_length:
                        found = False
                        break
                if found is True:
                    max_size = max(max_size, side_length)

    return max_size


"""
Approach:
1. Compute an aux matrix of same size as input matrix.
2. aux[i][j] = maximum size square sub-matrix with bin_matrix[i][j] as the bottom right corner.
3. aux[i][j] = min(aux[i-1][j], aux[i][j-1], aux[i-1][j-1])+1 if bin_matrix[i][j] == 1 else 0.
4. Return the max value from aux matrix.
"""


def max_sub_square(bin_matrix):

    aux_matrix = [[0] * len(row) for row in bin_matrix]
    max_size = -float('inf')
    for i in range(len(bin_matrix)):
        for j in range(len(bin_matrix[0])):
            aux_matrix[i][j] = bin_matrix[i][j]
            if i-1 >= 0 and j-1 >= 0 and bin_matrix[i][j] == 1:
                aux_matrix[i][j] = 1 + min(aux_matrix[i-1][j], aux_matrix[i][j-1], aux_matrix[i-1][j-1])
            max_size = max(max_size, aux_matrix[i][j])

    return max_size


class TestBinMatrix(unittest.TestCase):

    def test_bin_matrix(self):
        bin_matrix = [[0, 1, 1, 0, 1], [1, 1, 0, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1],
                      [0, 0, 0, 0, 0]]
        self.assertEqual(max_sub_square(bin_matrix), 3)
