import unittest
"""
Given an integer array, find the maximum product of a triplet in the array.
Input: 10 3 5 6 20
Output: 1200 (10 6 20)
"""


"""
Approach:
1. One way is to sort the array and return the product of the last three values.
2. A better way is to find the maximum, second maximum and third maximum.
3. Also find the minimum and second minimum.
4. Return the maximum of product between max, second max and third max and max, min and second min.
"""


def max_product_triplet(list_of_numbers):

    first_max = -float('inf')
    second_max = -float('inf')
    third_max = -float('inf')
    first_min = float('inf')
    second_min = float('inf')
    for i in range(len(list_of_numbers)):

        if list_of_numbers[i] > first_max:
            third_max = second_max
            second_max = first_max
            first_max = list_of_numbers[i]
        elif list_of_numbers[i] > second_max:
            third_max = second_max
            second_max = list_of_numbers[i]
        elif list_of_numbers[i] > third_max:
            third_max = list_of_numbers[i]

        if list_of_numbers[i] < first_min:
            second_min = first_min
            first_min = list_of_numbers[i]
        elif list_of_numbers[i] < second_min:
            second_min = list_of_numbers[i]

    return max(first_max * second_max * third_max, first_max * first_min * second_min)


class TestMaxProductTriplet(unittest.TestCase):

    def test_max_product_triplet(self):
        list_of_numbers = [1, -4, 3, -6, 7, 0]
        self.assertEqual(max_product_triplet(list_of_numbers), 168)

