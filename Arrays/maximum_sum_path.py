import unittest
"""
Given two sorted arrays such that the arrays may have some common elements, find the maximum sum path
to reach from beginning of any array to end of any array. We can switch from one array to another array
only at common elements.
Input: arr1: 2 3 7 10 12 arr2: 1 5 7 8
Output: 35 (1 + 5 + 7 + 10 + 12)
"""

"""
Approach:
1. Scan both arrays from left to right.
2. Keep two running sums, sum1 and sum2 for the two arrays.
3. Move pointer in array whose current element is smaller among the two, and add that element to
   respective running sum.
4. When the corresponding elements from the two arrays are equal, take max(sum1, sum2) till that point,
   and add the equal element to the max value.
5. Return the overall max sum as the maximum sum path.
"""


def maximum_sum_of_a_path(list1, list2):

    end1 = len(list1)
    end2 = len(list2)

    sum1 = 0
    sum2 = 0
    max_sum = 0

    i = 0
    j = 0

    while i < end1 and j < end2:
        if list1[i] < list2[j]:
            sum1 += list1[i]
            i += 1
        elif list1[i] > list2[j]:
            sum2 += list2[j]
            j += 1
        else:
            max_sum += max([sum1, sum2])
            max_sum += list1[i]
            i += 1
            j += 1
            sum1 = 0
            sum2 = 0

    while i < end1:
        sum1 += list1[i]
        i += 1

    while j < end2:
        sum2 += list2[j]
        j += 1

    max_sum += max([sum1, sum2])

    return max_sum


class TestMaxSumPath(unittest.TestCase):

    def test_max_sum_path(self):
        arr1 = [2, 3, 7, 10, 12]
        arr2 = [1, 5, 7, 8]

        self.assertEqual(maximum_sum_of_a_path(arr1, arr2), 35)

        arr1 = [10, 12]
        arr2 = [5, 7, 9]

        self.assertEqual(maximum_sum_of_a_path(arr1, arr2), 22)

        arr1 = [2, 3, 7, 10, 12, 15, 30, 34]
        arr2 = [1, 5, 7, 8, 10, 15, 16, 19]

        self.assertEqual(maximum_sum_of_a_path(arr1, arr2), 122)


