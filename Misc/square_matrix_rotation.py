"""
Given a square matrix, rotate it in-place 90 degrees anti-clockwise.
"""


def matrix_rotate(mat):
    N = len(mat[0])
    sz = N
    for layer in range(1, N/2 + 1):
        fR = fC = layer - 1
        lR = lC = N - layer

        for i in range(sz - 1):
            temp = mat[fR][lC - i]
            mat[fR][lC - i] = mat[lR - i][lC]
            mat[lR - i][lC] = mat[lR][fC + i]
            mat[lR][fC + i] = mat[fR + i][fC]
            mat[fR + i][fC] = temp

        sz /= 2


def print_matrix(mat):
    N = len(mat[0])
    for i in range(N):
        for j in range(N):
            print str(mat[i][j]) + " ",
        print '\n',


if __name__ == '__main__':
    mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print 'Before rotation: '
    print_matrix(mat)
    matrix_rotate(mat)
    print 'After rotation: '
    print_matrix(mat)
