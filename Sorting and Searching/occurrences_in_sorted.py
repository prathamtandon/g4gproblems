import unittest
"""
Given a sorted array arr[] and a number x, write a function that counts the occurrences of
x in arr[]. Expected time complexity is O(log(N)).
Input: 1 1 2 2 2 2 3, x = 2
Output: 4
Input: 1 1 2 2 2 2 3, x = 5
Output: -1
"""


"""
Approach:
1. Idea is to use binary search to find the first occurrence of x, say, i.
2. Then use binary search to find the last occurrence of x, say j.
3. Return count as j-i+1.
"""


def count_occurrences(arr, x):
    i = first_occurrence(arr, x, 0, len(arr)-1)
    if i == -1:
        return -1
    j = last_occurrence(arr, x, i, len(arr)-1)
    return j-i+1


def first_occurrence(arr, x, low, high):
    if low > high:
        return -1
    if arr[low] == x:
        return low
    mid = (low + high) / 2
    if mid > low and arr[mid] == x and arr[mid-1] != x:
        return mid
    if arr[mid] < x:
        return first_occurrence(arr, x, mid+1, high)
    return first_occurrence(arr, x, low, mid-1)


def last_occurrence(arr, x, low, high):
    if low > high:
        return -1
    if arr[high] == x:
        return high
    mid = (low + high) / 2
    if mid < high and arr[mid] == x and arr[mid+1] != x:
        return mid
    if arr[mid] > x:
        return last_occurrence(arr, x, low, mid-1)
    return last_occurrence(arr, x, mid+1, high)


class TestOccurrencesInSorted(unittest.TestCase):

    def test_occurrences(self):
        arr = [1, 1, 2, 2, 2, 2, 3]
        self.assertEqual(count_occurrences(arr, 2), 4)
        self.assertEqual(count_occurrences(arr, 4), -1)
