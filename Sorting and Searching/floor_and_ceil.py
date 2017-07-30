import unittest
"""
Given a sorted array and a value x, find the floor and ceiling of x.
floor(x) = largest value in the array <= x
ceil(x) = smallest value in the array >= x
"""


def floor(arr, x):
    if arr[0] > x:
        return -1
    n = len(arr)
    step = n
    p = 0
    while step >= 1:
        # Travel left to right in steps n, n/2, n/4 etc.
        while p + step < n and arr[p + step] <= x:
            p += step
        step /= 2
    return arr[p]


def ceil(arr, x):
    n = len(arr)
    if arr[n-1] < x:
        return -1
    step = n
    p = 2*n-1
    while step >= 1:
        # Travel right to left in steps n, n/2, n/4 etc.
        while p - step >= 0 and arr[p - step] >= x:
            p -= step
        step /= 2
    return arr[p]


class TestFloorCeil(unittest.TestCase):

    def test_floor_ceil(self):
        arr = [1, 2, 8, 10, 10, 12, 19]
        self.assertEqual(floor(arr, 0), -1)
        self.assertEqual(ceil(arr, 0), 1)
        self.assertEqual(floor(arr, 1), 1)
        self.assertEqual(ceil(arr, 1), 1)
        self.assertEqual(floor(arr, 5), 2)
        self.assertEqual(ceil(arr, 5), 8)
        self.assertEqual(floor(arr, 20), 19)
        self.assertEqual(ceil(arr, 20), -1)

