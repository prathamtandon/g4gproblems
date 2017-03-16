import heapq
import unittest
"""
Given an nxn matrix, where every row and column is sorted in ascending order. Find the
kth smallest element in the given 2D array.
Example:
        10, 20, 30, 40
        15, 25, 35, 45
        24, 29, 37, 48
        32, 33, 39, 50
The 3rd smallest element is 20 and 7th smallest element is 30
"""

"""
Approach:
1. The main idea is to use a min heap.
2. First create a min heap using first row of the 2D array.
3. The min heap entry will also contain the row and column numbers of the item.
4. Extract the minimum value from min heap, add the next number from its column and min-heapify.
5. Repeat step 4 k times. The root will represent kth smallest value.
"""


class Cell:
    def __init__(self, data, row, col):
        self.data = data
        self.row = row
        self.col = col

    def __le__(self, other):
        return self.data <= other.data


class SortedMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.min_heap = []
        self.num_rows = len(matrix)
        self.num_cols = len(matrix[0])

    def get_kth_smallest(self, k):
        self.create_min_heap_from(self.convert_row_to_cells(0))
        return self.get_kth_smallest_using_heap(k)

    def create_min_heap_from(self, data):
        self.min_heap = data[:]
        heapq.heapify(self.min_heap)

    def convert_row_to_cells(self, row_id):
        return [Cell(self.matrix[row_id][col_id], row_id, col_id) for col_id in range(self.num_cols)]

    def get_kth_smallest_using_heap(self, k):
        min_cell = None
        for i in range(k):
            min_cell = heapq.heappop(self.min_heap)
            if not self.has_next_in_column(min_cell):
                return -1
            heapq.heappush(self.min_heap, self.next_in_column(min_cell))
        return min_cell.data

    def has_next_in_column(self, cell):
        return (cell.row + 1) < self.num_rows

    def next_in_column(self, cell):
        row_id = cell.row + 1
        col_id = cell.col
        return Cell(self.matrix[row_id][col_id], row_id, col_id)


class TestSortedMatrix(unittest.TestCase):

    def test_sorted_matrix_get_kth_smallest(self):
        matrix = [[10, 20, 30, 40],
                  [15, 25, 35, 45],
                  [24, 29, 37, 48],
                  [32, 33, 39, 50]]
        sorted_matrix = SortedMatrix(matrix)
        self.assertEqual(sorted_matrix.get_kth_smallest(3), 20)
        self.assertEqual(sorted_matrix.get_kth_smallest(7), 30)

