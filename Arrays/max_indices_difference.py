import unittest
"""
Given an array of numbers, find the maximum (j-i) such that a[j] > a[i]
Input: 34 8 10 3 2 80 30 33 1
Output: 6 (j = 7, i = 1)
"""

"""
THIS IS NOT DO-ABLE IN THE MOST EFFICIENT MANNER WITHOUT KNOWING THE SOLN.
Approach:
1. Create two auxiliary arrays min_to_my_left and max_to_my_right.
2. As the names suggest, min_to_my_left[i] = minimum element to my left including me.
3. Other array is defined similarly.
4. Once, we have the arrays, we scan from left to right.
5. If min_to_my_left[i] > max_to_my_right[j], we move i forward, since smaller elements can only be found
   to the right of min_to_my_left[i]
6. If max_to_my_right[j] > min_to_my_left[i], we compute j-i, compare against max, and move j forward,
   since there may be other elements to right which are larger.
7. Return max j-i found from above steps.
"""

"""
Approach 2.
This approach uses BST. Insert array elements one by one into a BST.
Whenever, we move to a right link (ie new item > current node), we take diff between
new item index with node index, and return the max diff found at the end.
"""


def maximum_indices_difference(list_of_numbers):
    list_length = len(list_of_numbers)
    min_to_my_left = [list_of_numbers[0]] * list_length
    max_to_my_right = [list_of_numbers[list_length - 1]] * list_length

    for i in range(1, list_length):
        min_to_my_left[i] = min(list_of_numbers[i], min_to_my_left[i-1])

    for j in reversed(range(0, list_length - 1)):
        max_to_my_right[j] = max(list_of_numbers[j], max_to_my_right[j+1])

    i = 0
    j = 0
    max_difference = -1

    while i < list_length and j < list_length:
        if max_to_my_right[j] > min_to_my_left[i]:
            max_difference = max(max_difference, j-i)
            j += 1
        else:
            i += 1

    return max_difference


class TestMaxIndicesDiff(unittest.TestCase):

    def test_max_indices_diff(self):
        list_of_numbers = [34, 8, 10, 3, 2, 80, 30, 33, 1]
        self.assertEqual(maximum_indices_difference(list_of_numbers), 6)
        list_of_numbers = [6, 5, 4, 3, 2, 1]
        self.assertEqual(maximum_indices_difference(list_of_numbers), -1)

