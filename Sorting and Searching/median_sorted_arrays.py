import unittest
"""
There are two sorted arrays A and B of size n each. Write an algorithm
to find the median of the array obtained after merging the above two arrays.
"""


"""
Approach: (Not intuitive)
1. Let m1 be the median of arr1 and m2 be the median of arr2.
2. If m1 == m2, return m1.
3. If m1 > m2, then compare arr1[0...m1] and arr2[m2...n-1]
4. If m1 < m2, then compare arr1[m1...n-1] and arr2[0...m2]
5. Handle base case where len(arr1) == len(arr2) = 2.
"""


def median(arr):
    n = len(arr)
    mid = n/2
    if n % 2 == 0:
        return (arr[mid] + arr[mid-1])/2
    return arr[mid]


def median_sorted_arrays(arr1, arr2):
    assert len(arr1) == len(arr2)
    if len(arr1) == 1:
        return (arr1[0] + arr2[0]) / 2
    if len(arr1) == 2:
        return (max(arr1[0], arr2[0]) + min(arr1[1], arr2[1])) / 2
    n = len(arr1)
    median1 = median(arr1)
    median2 = median(arr2)
    if median1 == median2:
        return median1
    if median1 > median2:
        if n % 2 == 0:
            return median_sorted_arrays(arr1[:n/2], arr2[n/2:])
        return median_sorted_arrays(arr1[:(n/2+1)], arr2[n/2:])
    if n % 2 == 0:
        return median_sorted_arrays(arr1[n/2:], arr2[:n/2])
    return median_sorted_arrays(arr1[n/2:], arr2[:(n/2+1)])


class TestMedianSorted(unittest.TestCase):

    def test_median(self):
        arr1 = [4, 17, 25]
        arr2 = [5, 15, 30]

        self.assertEqual(median_sorted_arrays(arr1, arr2), 16)

        arr1 = [1, 2, 3, 6]
        arr2 = [4, 6, 8, 10]

        self.assertEqual(median_sorted_arrays(arr1, arr2), 5)
