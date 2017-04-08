import unittest
"""
Given an array of integers, arrange the array such that first element is maximum,
second element is minimum, third element is second maximum, fourth element is second minimum and so on.
Input: 1 2 3 4 5 6 7
Output: 7 1 6 2 5 3 4
Expected space complexity is O(1).
"""

"""
Approach:
1. The idea is to use a trick to store two elements at same index in the array.
2. If arr[i], arr[j] are positive integers arr[i] < n and arr[j] < n, then if we make arr[i] = arr[i] + arr[j]*n,
   then arr[i]/n gives arr[j] and arr[i]%n gives arr[i].
3. This is a general trick which can be used in other rearrange type of problems as well.
"""


def rearrange_max_min(arr):
    arr = sorted(arr)
    n = len(arr)
    max_index = n-1
    min_index = 0
    max_elem = arr[n-1] + 1  # this element is guaranteed bigger than all elements in the array

    for i in range(n):
        if i % 2 == 0:
            arr[i] += (arr[max_index] % max_elem) * max_elem
            max_index -= 1
        else:
            arr[i] += (arr[min_index] % max_elem) * max_elem
            min_index += 1

    return [x / max_elem for x in arr]


class TestRearrange(unittest.TestCase):

    def test_rearrange(self):
        list_of_numbers = [3, 1, 2, 4, 6, 5, 7]
        list_of_numbers = rearrange_max_min(list_of_numbers)
        self.assertEqual(list_of_numbers, [7, 1, 6, 2, 5, 3, 4])
        list_of_numbers = [3, 1, 2, 7, 6, 5, 7]
        list_of_numbers = rearrange_max_min(list_of_numbers)
        self.assertEqual(list_of_numbers, [7, 1, 7, 2, 6, 3, 5])
