import unittest
"""
Three way quicksort is used when array has lot of repeating elements.
In 3 way quicksort, following is the partitioning:
1. arr[low...i] < pivot
2. arr[i+1...j-1] == pivot
3. arr[j...high] > pivot
NOTE: Assume pivot is last element.
"""

"""
Approach:
We can approach it in same way as sort an array of 0s,1s and 2s. (Dutch national flag problem)
"""


def quicksort_3_way_partition(arr, low, high):

    pivot = arr[high]
    mid = low

    while mid <= high:
        if arr[mid] < pivot:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == pivot:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return low-1, mid


class TestQuickSort(unittest.TestCase):

    def test_quicksort(self):
        arr = [4, 9, 4, 4, 1, 9, 4, 4, 9, 4, 4, 1, 4]
        n = len(arr)
        self.assertEqual(quicksort_3_way_partition(arr, 0, n-1), (1, 10))
