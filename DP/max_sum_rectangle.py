import unittest
"""
Given a 2D array, find the maximum sum subarray in it.
"""

"""
Approach:
1. The idea is to try left and right boundaries of the rectangle one by one.
2. For each left and right boundary selected, we find the sum of all cells from left to right.
3. Say, there is an array temp - so temp[i] stores the sum of cells from left to right boundary for row i.
4. i will vary from 0 to num_rows-1.
5. Now, if we run Kadane's algorithm to find the maximum sum subarray, the starting and ending index of this
    array gives the best rectangle for given left and right boundaries.
6. Compare with best rectangle so far and update if required.
"""


def kadane(arr):
    max_so_far = -float('inf')
    running_sum = 0
    start = -1
    finish = -1
    local_start = 0
    for i in range(len(arr)):
        running_sum += arr[i]
        if running_sum < 0:
            running_sum = 0
            local_start = i+1
        elif running_sum > max_so_far:
            max_so_far = running_sum
            start = local_start
            finish = i

    # There is at-least one non-negative number
    if finish != -1:
        return max_so_far, start, finish

    # Special case: When all numbers are negative
    max_so_far = -float('inf')
    for i in range(len(arr)):
        if arr[i] > max_so_far:
            max_so_far = arr[i]
            start = i
            finish = i

    return max_so_far, start, finish


def maximum_sum_rectangle(matrix):

    num_rows = len(matrix)
    num_cols = len(matrix[0])
    max_so_far = -float('inf')
    max_left = 0
    max_right = 0
    max_top = 0
    max_bottom = 0

    for left in range(num_cols):
        temp = [0] * num_rows
        for right in range(left, num_cols):
            for i in range(num_rows):
                temp[i] += matrix[i][right]
            running_sum, start, finish = kadane(temp)
            if running_sum > max_so_far:
                max_so_far = running_sum
                max_left = left
                max_right = right
                max_top = start
                max_bottom = finish

    return max_so_far, max_left, max_right, max_top, max_bottom


class TestMaximumSumRectangle(unittest.TestCase):

    def test_max_sum_rectangle(self):
        matrix = [[1, 2, -1, -4, -20],
                  [-8, -3, 4, 2, 1],
                  [3, 8, 10, 1, 3],
                  [-4, -1, 1, 7, -6]]
        max_so_far, max_left, max_right, max_top, max_bottom = maximum_sum_rectangle(matrix)
        self.assertEqual(max_so_far, 29)
        self.assertEqual(max_left, 1)
        self.assertEqual(max_right, 3)
        self.assertEqual(max_top, 1)
        self.assertEqual(max_bottom, 3)
