import unittest
"""
Given an array of only 0s, 1s and 2s, sort the array in ascending order.
"""

"""
Approach:
1. The idea is to partition the array into three parts.
2. The first part A[1...Lo-1] denotes where 0s are placed.
3. The second part A[Lo...Mid-1] denotes where 1s are placed.
4. The third part A[Mid...Hi] denotes where 2s are placed.
"""


def sort_012(arr):
    lo = 0
    hi = len(arr)-1
    mid = 0

    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1

    return arr


class TestSort(unittest.TestCase):

    def test_sort(self):
        arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
        self.assertEqual(sort_012(arr), [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2])

