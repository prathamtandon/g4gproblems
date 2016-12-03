import unittest
"""
Given an array A of size n, where every element is between 0 and n-1, rearrange given array
such that A[i] becomes A[A[i]].
Input: 3 2 0 1
Output: 1 0 3 2
"""

"""
Approach:
Frankly, don't really know why it works!
1. Increment each A[i] by (A[A[i]]%n)*n.
2. Divide each A[i] by n.
"""


def rearrange_array_elements(list_of_numbers):

    n = len(list_of_numbers)
    for i in range(n):
        list_of_numbers[i] += (list_of_numbers[list_of_numbers[i]] % n) * n

    list_of_numbers = [x/n for x in list_of_numbers]

    return list_of_numbers


class TestRearrangeArray(unittest.TestCase):

    def test_rearrange(self):
        list_of_numbers = [3, 2, 0, 1]
        self.assertEqual(rearrange_array_elements(list_of_numbers), [1, 0, 3, 2])
