import unittest
"""
Given a sorted array and a value x, find the floor and ceiling of x.
floor(x) = largest value in the array <= x
ceil(x) = smallest value in the array >= x
"""


def floor_helper(arr, x, low, high):

    if low > high:
        return -1
    if x >= arr[high]:
        return arr[high]
    mid = low + (high - low) / 2
    if arr[mid] == x:
        return x
    # check if mid - 1 is floor
    if mid > 0 and arr[mid - 1] <= x < arr[mid]:
        return arr[mid - 1]
    if arr[mid] > x:
        return floor_helper(arr, x, low, mid - 1)
    return floor_helper(arr, x, mid + 1, high)


def ceil_helper(arr, x, low, high):

    while low < high:
        mid = low + (high - low) / 2
        if arr[mid] == x:
            return x
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid

    return arr[high]


def floor(arr, x):
    n = len(arr)
    return floor_helper(arr, x, 0, n-1)


def ceil(arr, x):
    n = len(arr)
    res = ceil_helper(arr, x, 0, n-1)
    if res >= x:
        return res
    return -1


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

