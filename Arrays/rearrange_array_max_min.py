import unittest
"""
Given a sorted array of positive integers, rearrange the array such that first element
is max, second element is min, third element is second max, fourth element is second min and so on.
Input: 1 2 3 4 5 6 7
Output: 7 1 6 2 5 3 4
Input: 1 2 3 4 5 6
Output: 6 1 5 2 4 3
"""

"""
Approach:
1. Create an index array such that index[i] contains the correct output position for arr[i].
2. Swap elements by following the indices as specified by index array.
"""


def rearrange_max_min(list_of_numbers):

    end = len(list_of_numbers)
    max_i = end-1
    min_i = 0
    index = []

    while len(index) != end:
        index.append(max_i)
        if max_i != min_i:
            index.append(min_i)
        max_i -= 1
        min_i += 1

    for i in range(end):
        if list_of_numbers[i] < 0:
            continue
        j = i
        k = index[i]
        while k != i:
            list_of_numbers[j], list_of_numbers[k] = list_of_numbers[k], list_of_numbers[j]
            list_of_numbers[j] = -list_of_numbers[j]
            k = index[index[j]]
            j = index[j]
        list_of_numbers[j] = -list_of_numbers[j]

    list_of_numbers = [-x for x in list_of_numbers]
    return list_of_numbers


class TestRearrange(unittest.TestCase):

    def test_rearrange(self):
        list_of_numbers = [1, 2, 3, 4, 5, 6, 7]
        result = rearrange_max_min(list_of_numbers)
        self.assertEqual(result, [7, 1, 6, 2, 5, 3, 4])


