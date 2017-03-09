import unittest
"""
Given a list of integers, find a peak element. A peak element A[i] is defined as: A[i-1] <= A[i] >= A[i+1].
Expected time complexity is O(log(N)).
Input: 5 10 20 15
Output: 20
"""


def peak_helper(arr, low, high):
    if low == high:
        return arr[low]
    elif low + 1 == high:
        return max(arr[low], arr[high])
    mid = (low + high) / 2
    if arr[mid-1] <= arr[mid] >= arr[mid+1]:
        return mid
    if arr[mid-1] > arr[mid]:
        return peak_helper(arr, low, mid - 1)
    return peak_helper(arr, mid + 1, high)


def valley_helper(arr, low, high):
    if low == high:
        return arr[low]
    elif low + 1 == high:
        return min(arr[low], arr[high])
    mid = (low + high) / 2
    if arr[mid-1] >= arr[mid] <= arr[mid+1]:
        return mid
    if arr[mid-1] < arr[mid]:
        return valley_helper(arr, low, mid-1)
    return valley_helper(arr, mid+1, high)


def valley(arr):
    return valley_helper(arr, 0, len(arr)-1)


def peak(arr):
    return peak_helper(arr, 0, len(arr)-1)


class TestPeak(unittest.TestCase):

    def test_peak(self):
        arr = [5, 10, 20, 15]
        self.assertEqual(peak(arr), 20)
        arr = [1, 2, 3, 4]
        self.assertEqual(peak(arr), 4)
        arr = [10, 9, 8, 7, 6]
        self.assertEqual(peak(arr), 10)

    def test_valley(self):
        arr = [11, 10, 9, 15]
        self.assertEqual(valley(arr), 9)
        arr = [1, 2, 3, 4]
        self.assertEqual(valley(arr), 1)
        arr = [10, 9, 8, 7, 6]
        self.assertEqual(valley(arr), 6)

