import unittest
"""
Given a maze with obstacles, count number of paths to reach bottom-right cell from top-left cell.
If a cell in maze has value -1, then its an obstacle or dead end, else it has value 0. For a given cell
(i,j) we are allowed to move only to (i+1,j) and (i,j+1)
"""

"""
Approach:
1. Let table[i][j] denote number of ways to reach cell (i,j) from (0,0).
2. If maze[i][j] is -1, then table[i][j] is -1.
3. If maze[i-1][j] is > 0, then table[i][j] += maze[i-1][j].
4. If maze[i][j-1] is > 0, then table[i][j] += maze[i-1][j].
"""


def maze_paths(maze):

    if maze[0][0] == -1:
        return 0
    num_rows = len(maze)
    num_cols = len(maze[0])

    #  All cells in first column can be reached only from the cell above them.
    for i in range(1, num_rows):
        if maze[i][0] == 0:
            maze[i][0] = 1
        else:
            break
    #  All cells in first row can be reached only from cell to their left.
    for i in range(1, num_cols):
        if maze[0][i] == 0:
            maze[0][i] = 1
        else:
            break

    for i in range(1, num_rows):
        for j in range(1, num_cols):
            if maze[i][j] == -1:
                continue
            if maze[i-1][j] > 0:
                maze[i][j] += maze[i-1][j]
            if maze[i][j-1] > 0:
                maze[i][j] += maze[i][j-1]

    if maze[num_rows-1][num_cols-1] > 0:
        return maze[num_rows-1][num_cols-1]
    else:
        return 0


class TestMazeTraversal(unittest.TestCase):

    def test_maze_traversal(self):
        maze = [[0, 0, 0, 0],
                [0, -1, 0, 0],
                [-1, 0, 0, 0],
                [0, 0, 0, 0]]
        self.assertEqual(maze_paths(maze), 4)
