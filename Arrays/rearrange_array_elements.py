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


def rearrange_array_elements(arr):

    n = len(arr)
    for i in range(n):
        a = arr[i]
        b = arr[arr[i]]
        c = a + (b % n)*n
        arr[i] = c

    arr = [c / n for c in arr]
    # To get back original array, do:
    # arr = [c % n for c in arr]

    return arr


class TestRearrangeArray(unittest.TestCase):

    def test_rearrange(self):
        list_of_numbers = [3, 2, 0, 1]
        self.assertEqual(rearrange_array_elements(list_of_numbers), [1, 0, 3, 2])
