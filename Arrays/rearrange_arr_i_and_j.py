import unittest
"""
Given an array of size n, where each element is between 0 and n-1, change the contents of arr[]
so that arr[i] = j is changed to arr[j] = i.
Input: arr[] = 1 3 0 2
Output: arr[] = 2 0 3 1
"""

"""
Approach is similar to problem in rearrange_array_elements.py
"""


def rearrange_arr_i_and_j(list_of_numbers):

    end = len(list_of_numbers)

    for i in range(end):
        j = list_of_numbers[i] % end
        list_of_numbers[j] += i * end

    list_of_numbers = [x / end for x in list_of_numbers]

    return list_of_numbers


class TestRearrange(unittest.TestCase):

    def test_rearrange(self):
        list_of_numbers = [2, 0, 1, 4, 5, 3]
        self.assertEqual(rearrange_arr_i_and_j(list_of_numbers), [1, 2, 0, 5, 3, 4])
        list_of_numbers = [1, 3, 0, 2]
        self.assertEqual(rearrange_arr_i_and_j(list_of_numbers), [2, 0, 3, 1])
