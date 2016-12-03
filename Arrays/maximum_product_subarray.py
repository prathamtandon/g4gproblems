import unittest
"""
Given an array that contains both positive and negative integers, find the product
of the maximum product subarray.
Input: 6 -3 -10 0 2
Output: 180
Input: -1 -3 -10 0 60
Output: 60
Input: -2 -3 0 -2 -40
Output: 80
"""

"""
Approach:
1. At each position in array, there are questions to answer:
(a) Can we obtain the maximum product by multiplying previous maximum product by current element?
(This happens when current element is positive)
(b) Can we obtain the maximum product by multiplying previous minimum product by current element?
(This happens when current element is negative)
(c) Should we start a new largest product subarray from this element?
These three choices are summed up in code below.
"""


def find_maximum_product_subarray(list_of_numbers):

    prev_max_product = list_of_numbers[0]
    prev_min_product = list_of_numbers[0]
    max_answer = -float('inf')

    for i in range(1, len(list_of_numbers)):
        cur_max_product = max(prev_max_product*list_of_numbers[i],
                              prev_min_product*list_of_numbers[i],
                              list_of_numbers[i])
        cur_min_product = min(prev_max_product*list_of_numbers[i],
                              prev_min_product*list_of_numbers[i],
                              list_of_numbers[i])
        max_answer = max(max_answer, cur_max_product)
        prev_max_product = cur_max_product
        prev_min_product = cur_min_product

    return max_answer


class TestMaxProductSubarray(unittest.TestCase):

    def test_max_product_subarray(self):
        list_of_numbers = [-6, -3, -10]
        self.assertEqual(find_maximum_product_subarray(list_of_numbers), 30)
        list_of_numbers = [6, -3, -10, 0, 2]
        self.assertEqual(find_maximum_product_subarray(list_of_numbers), 180)
        list_of_numbers = [-2, -3, 0, -2, -40]
        self.assertEqual(find_maximum_product_subarray(list_of_numbers), 80)
        list_of_numbers = [0, 0, -3, 0, 0]
        self.assertEqual(find_maximum_product_subarray(list_of_numbers), 0)
