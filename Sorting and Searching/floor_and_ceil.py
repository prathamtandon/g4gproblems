import unittest
"""
Given a sorted array and a value x, find the floor and ceiling of x.
floor(x) = largest value in the array <= x
ceil(x) = smallest value in the array >= x
"""


def floor(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == x:
            return x
        if arr[mid] < x:
            ans = arr[mid]
            low = mid + 1
        else:
            high = mid - 1

    return ans


def ceil(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) / 2
        if arr[mid] == x:
            return x
        if arr[mid] > x:
            ans = arr[mid]
            high = mid - 1
        else:
            low = mid + 1

    return ans


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

