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
    ans = -1
    while low <= high:
        mid = low + (high - low) / 2
        if arr[mid] == x:
            ans = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return ans


def last_occurrence(arr, x, low, high):
    ans = -1
    while low <= high:
        mid = low + (high - low) / 2
        if arr[mid] == x:
            ans = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return ans


class TestOccurrencesInSorted(unittest.TestCase):

    def test_occurrences(self):
        arr = [1, 1, 2, 2, 2, 2, 3]
        self.assertEqual(count_occurrences(arr, 2), 4)
        self.assertEqual(count_occurrences(arr, 4), -1)
