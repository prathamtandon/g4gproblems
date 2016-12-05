import unittest
"""
Given an array of integers and a number x, find the smallest subarray with sum greater
than the x.
 Input: 1 4 45 6 0 19
     x: 51
Output: 3
"""

"""
Approach:
Modify the "Find a subarray with sum equal to given value" algorithm.
"""


def smallest_subarray_with_larger_sum(list_of_numbers, x):

    running_sum = 0
    min_length = float('inf')
    start = 0

    for end in range(len(list_of_numbers)):

        while start <= end - 1 and running_sum > x:
            if running_sum - list_of_numbers[start] <= x:
                min_length = min([min_length, end - start])
                break
            running_sum -= list_of_numbers[start]
            start += 1

        running_sum += list_of_numbers[end]

    return min_length


class TestSmallestSubarray(unittest.TestCase):

    def test_smallest_subarray(self):
        list_of_numbers = [1, 4, 45, 6, 10, 19]
        self.assertEqual(smallest_subarray_with_larger_sum(list_of_numbers, 51), 3)
        list_of_numbers = [1, 10, 5, 2, 7]
        self.assertEqual(smallest_subarray_with_larger_sum(list_of_numbers, 9), 1)
        list_of_numbers = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
        self.assertEqual(smallest_subarray_with_larger_sum(list_of_numbers, 280), 4)
        list_of_numbers = [10, 16, 5, 25, 4]
        self.assertEqual(smallest_subarray_with_larger_sum(list_of_numbers, 28), 2)
