import unittest
"""
An element in a sorted array can be found in O(logN) time using Binary Search.
But suppose, we rotate an ascending order sorted array by an unknown amount. So
for instance, 1 2 3 4 5 may become 3 4 5 1 2. Devise a way to find an element in
rotated array in O(logN) time.
"""

"""
Approach:
1. The idea is to find a pivot element in rotated array.
2. A pivot element is such that element next to it is smaller than it. (Eg. 5 in above example)
3. Once we find such an element, we know the subarrays to its left and right are already sorted.
   So we can do a normal Binary Search on one of the two subarrays.
4. The trick is to find the pivot element in O(logN) time.
"""


def find_pivot(arr, low, high):
    if low > high:
        return -1
    mid = (low + high) / 2
    if mid < high and arr[mid] > arr[mid+1]:
        return mid
    if low < mid and arr[mid] < arr[mid-1]:
        return mid-1
    if arr[low] > arr[mid]:
        return find_pivot(arr, low, mid-1)
    elif arr[mid] > arr[high]:
        return find_pivot(arr, mid+1, high)
    else:
        # Handle test cases 2 and 3 as mentioned in test runner.
        left = find_pivot(arr, low, mid-1)
        right = find_pivot(arr, mid+1, high)
        if left == -1 and right == -1:
            return -1
        return left if left != -1 else right


def binary_search(arr, low, high, key):
    if low > high:
        return -1
    mid = (low + high) / 2
    if arr[mid] == key:
        return mid
    if arr[mid] < key:
        return binary_search(arr, mid+1, high, key)
    return binary_search(arr, low, mid-1, key)


def search_sorted_rotated(arr, key):
    n = len(arr)
    pivot = find_pivot(arr, 0, n-1)
    if pivot == -1:
        return binary_search(arr, 0, n-1, key)
    if arr[pivot] == key:
        return pivot
    if arr[0] < key:
        return binary_search(arr, 0, pivot-1, key)
    return binary_search(arr, pivot+1, n-1, key)


class TestSearchSortedRotated(unittest.TestCase):

    def test_search_sorted_rotated(self):
        arr = [3, 4, 5, 1, 2]
        self.assertEqual(search_sorted_rotated(arr, 1), 3)
        arr = [2, 2, 2, 2, 2, 0, 2]
        self.assertEqual(search_sorted_rotated(arr, 0), 5)
        arr = [2, 0, 2, 2, 2, 2, 2]
        self.assertEqual(search_sorted_rotated(arr, 0), 1)

