import unittest
"""
We are given two sorted arrays. We need to merge these two arrays such that
the initial numbers in the complete sorted array are in first array and remaining numbers are in second
array.
Input: arr1[]: 10
       arr2[]: 2, 3
Output: arr1[]: 2
        arr2[]: 3, 10
"""

"""
Approach:
1. Start at the last element of arr2 and move toward left.
2. For each element of arr2, compare with elements in arr1 from right to left.
3. Store last element of arr1 in temp, move elements to right until we find the correct place for element from arr2.
4. Once we find the correct place, place last element from arr2 in arr1 and place temp in arr2.
5. Time complexity is O(m*n)
"""


def merge_sorted_no_extra_space(first_sorted, second_sorted):

    first_end = len(first_sorted)
    second_end = len(second_sorted)
    j = 0
    for i in range(second_end-1, -1, -1):
        last = first_sorted[first_end-1]
        for j in range(first_end-2, -1, -1):
            if first_sorted[j] > second_sorted[i]:
                first_sorted[j+1] = first_sorted[j]
            else:
                break
        if j != first_end-2:
            first_sorted[j+1] = second_sorted[i]
            second_sorted[i] = last


class TestMerge(unittest.TestCase):

    def test_merge(self):
        first_sorted = [1, 5, 9, 10, 15, 20]
        second_sorted = [2, 3, 8, 13]
        merge_sorted_no_extra_space(first_sorted, second_sorted)
        self.assertEqual(first_sorted, [1, 2, 3, 5, 8, 9])
        self.assertEqual(second_sorted, [10, 13, 15, 20])

