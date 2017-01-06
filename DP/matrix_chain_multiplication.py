import unittest
"""
Given a sequence of matrices, find the most efficient way to multiply these together.
The order in which matrices are multiplied determines how many multiplications are performed.
For example, the multiplication ABCD can be performed in 3 different ways:
(A)(BCD)
(AB)(CD)
(ABC)(D)
We need to return the placement among these n-1 placements that has minimum number of operations.
"""


# dimensions[i-1] X dimensions[i] denotes the dimensions of matrix A[i]
def matrix_chain_multiplication(dimensions):
    # table[i][j] is minimum operations for multiplying the chain A[i...j]
    # table[1][N-1] will store the result for the chain A[1...N]
    table = [[float('inf')] * len(dimensions) for _ in range(len(dimensions))]
    for i in range(1, len(dimensions)):
        table[i][i] = 0

    for chain_length in range(2, len(dimensions)):
        for i in range(1, len(dimensions)-chain_length+1):
            j = i+chain_length-1
            for k in range(i, j):
                table[i][j] = min(table[i][j],
                                  table[i][k] + table[k+1][j] + dimensions[i-1]*dimensions[k]*dimensions[j])

    return table[1][len(dimensions)-1]


class TestMatrixChain(unittest.TestCase):

    def test_matrix_chain(self):
        dimensions = [1, 2, 3, 4]  # A[1] is 1X2, A[2] is 2X3 and A[3] is 3X4
        self.assertEqual(matrix_chain_multiplication(dimensions), 18)
