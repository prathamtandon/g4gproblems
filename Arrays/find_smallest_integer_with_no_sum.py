import unittest
"""
Given a sorted array of positive numbers, find the smallest positive integer value that
cannot be represented as sum of any subset of given array.
Input: 1 3 6 10 11 15
Output: 2
Input: 1 1 1 1
Output: 5
Input: 1 1 3 4
Output: 10
Input: 1 2 5 10 20 40
Output: 4
Input: 1 2 3 4 5 6
Output: 22
"""

"""
Approach:
1. Scan the array from left to right.
2. Keep a running sum starting at 1 => the least possible outcome.
3. Let 'res' be the minimum sum that can be represented from arr[0...i-1]
4. At arr[i], we have two choice to make:
    NOTE: If c = a + b and a > 0 and b > 0, then it follows that c > a and c > b. That is, in order to
    represent a value as a sum of other values, the other values must be smaller than sum.
    (a) res is the final result: This is the case when arr[i] is bigger than res, we know res cannot be represented
    by numbers following arr[i] as they are all bigger than arr[i]
    (b) res is incremented by arr[i]: This happens when arr[i] <= res. If arr[0...i-1] can represent res-1,
    then arr[0...i] can represent arr[i] + res - 1.
"""


def find_smallest_integer_with_no_equivalent_sum(list_of_numbers):

    res = 1
    end = len(list_of_numbers)

    for i in range(end):
        if list_of_numbers[i] <= res:
            res += list_of_numbers[i]
        else:
            return res

    return res


class TestSmallestInteger(unittest.TestCase):

    def test_smallest_integer(self):
        list_of_numbers = [1, 3, 4, 5]
        self.assertEqual(find_smallest_integer_with_no_equivalent_sum(list_of_numbers), 2)
        list_of_numbers = [1, 2, 6, 10, 11, 15]
        self.assertEqual(find_smallest_integer_with_no_equivalent_sum(list_of_numbers), 4)
        list_of_numbers = [1, 1, 3, 4]
        self.assertEqual(find_smallest_integer_with_no_equivalent_sum(list_of_numbers), 10)
