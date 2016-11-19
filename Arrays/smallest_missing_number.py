import unittest
"""
Given a sorted array of n integers, where each integer is in the range from 0 to m-1 and m > n,
find the smallest number which is missing from the array.
Input: 0 1 2 6 9, n = 5, m = 10
Output: 3
Input: 4 5 10 11, n = 4, m = 12
Output: 0
Input: 0 1 2 3, n = 4, m = 5
Output: 4
"""

"""
Approach
DAMN!
1. Use modified Binary Search.
2. First, check if first element is same as first index. If not, return first index.
3  Compute mid, and compare arr[mid] and mid.
4. If arr[mid] > mid, then required element is in left half else required element is in right half.
"""


def find_smallest_missing_binary_search(list_of_numbers, low, high):
    if low > high or list_of_numbers[low] != low:
        return low
    mid = low + (high - low) / 2
    if list_of_numbers[mid] > mid:
        return find_smallest_missing_binary_search(list_of_numbers, low, mid - 1)
    else:
        return find_smallest_missing_binary_search(list_of_numbers, mid + 1, high)


def find_smallest_missing(list_of_numbers, m):
    return find_smallest_missing_binary_search(list_of_numbers, 0, len(list_of_numbers) - 1)


class TestSmallestMissing(unittest.TestCase):

    def test_smallest_missing(self):
        list_of_numbers = [0, 1, 2, 6, 9]
        self.assertEqual(find_smallest_missing(list_of_numbers, 10), 3)
        list_of_numbers = [4, 5, 10, 11]
        self.assertEqual(find_smallest_missing(list_of_numbers, 12), 0)
        list_of_numbers = [0, 1, 2, 3]
        self.assertEqual(find_smallest_missing(list_of_numbers, 5), 4)
