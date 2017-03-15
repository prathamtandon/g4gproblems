"""
Given a matrix where every element is either 'O' or 'X', replace 'O'
with 'X' if surrounded by 'X'. A 'O' (or a set of 'O') is considered
to be surrounded by 'X' if there are 'X' at locations just below, just
above, just left and just right of it.
Input: mat[M][N] =  {{'X', 'X', 'X', 'X'}
                     {'X', 'O', 'X', 'X'}
                     {'X', 'O', 'O', 'X'}
                     {'X', 'O', 'X', 'X'}
                     {'X', 'X', 'O', 'O'}
                    };
Output: mat[M][N] =  {{'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'X', 'X'}
                     {'X', 'X', 'O', 'O'}
                    };
"""

"""
Approach:
1. The idea is to use Flood-fill algorithm.
2. First traverse the matrix and mark all 'O' with a special character like '-'.
3. Then, traverse the four edges, and if we encounter a '-', we run flood_fill('-', 'O')
4. After this, whatever '-' remain in matrix, are the ones which must be replaced with 'X'.
"""


def replace_o_x(matrix):

    R = len(matrix)
    C = len(matrix[0])

    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 'O':
                matrix[i][j] = '-'

    # traverse top edge
    for i in range(C):
        if matrix[0][i] == '-':
            flood_fill(matrix, 0, i, '-', 'O')

    # traverse right edge
    for i in range(R):
        if matrix[i][C-1] == '-':
            flood_fill(matrix, i, C-1, '-', 'O')

    # traverse bottom edge
    for i in range(C):
        if matrix[R-1][i] == '-':
            flood_fill(matrix, R-1, i, '-', 'O')

    # traverse left edge
    for i in range(R):
        if matrix[i][0] == '-':
            flood_fill(matrix, i, 0, '-', 'O')

    # replace remaining '-' with 'X'
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == '-':
                matrix[i][j] = 'X'

    return matrix


def flood_fill(matrix, row, col, old_color, new_color):
    R = len(matrix)
    C = len(matrix[0])
    if row < 0 or row >= R:
        return
    if col < 0 or col >= C:
        return
    if matrix[row][col] != old_color:
        return
    matrix[row][col] = new_color
    flood_fill(matrix, row-1, col, old_color, new_color)
    flood_fill(matrix, row, col+1, old_color, new_color)
    flood_fill(matrix, row+1, col, old_color, new_color)
    flood_fill(matrix, row, col-1, old_color, new_color)

