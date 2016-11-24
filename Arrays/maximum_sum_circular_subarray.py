import unittest
"""
Given n numbers, both positive and negative, arranged in a circle, find the maximum of
consecutive numbers.
Input: 8 -8 9 -9 10 -11 12
Output: 22 (12 8 -8 9 -9 10)
Input: 10 -3 -4 7 6 5 -4 -1
Output: 23 (7 6 5 -4 -1 10)
"""

"""
DIFFERENT LEVEL QUESTION!
Approach:
1. There are two simple cases: The maximum sum subarray does not wrap around OR it wraps around.
2. For first case, we can simply run Kadane's algorithm.
3. Second case is tricky.
4. Imagine it this way: When wrap around happens, we have 3 portions in the array:
    (a) Left portion of wrapped result
    (b) Excluded portion
    (c) Right portion of wrapped result.
5. What we want is to find the maximum possible value for (left portion of wrapped) + (right portion of wrapped).
6. Here is the trick: The above equation is same as : total sum of array - minimum possible value of excluded portion!
7. Now, the minimum possible portion itself is a subarray of the original array.
8. If we flip the sign of numbers in the array, and run Kadane's maximum sum subarray algorithm, what we will get
   will in reality be the minimum sum contiguous subarray. This can be substituted in (6) above.
9. Now we compare the results from the two cases and return the max amongst the two.
"""


def find_maximum_sum_subarray(list_of_numbers):

    max_so_far = -float('inf')
    max_ending_here = 0

    for i in range(len(list_of_numbers)):
        max_ending_here += list_of_numbers[i]
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_ending_here > max_so_far:
            max_so_far = max_ending_here

    return max_so_far


def find_maximum_sum_circular_subarray(list_of_numbers):

    max_non_wrapped_sum = find_maximum_sum_subarray(list_of_numbers)
    total_sum = 0

    for i in range(len(list_of_numbers)):
        total_sum += list_of_numbers[i]
        list_of_numbers[i] = -list_of_numbers[i]

    # wrapped_sum = total_sum - (-max subarray sum of inverted array)
    max_wrapped_sum = total_sum + find_maximum_sum_subarray(list_of_numbers)
    return max([max_non_wrapped_sum, max_wrapped_sum])


class TestMaxSumCircularSubarray(unittest.TestCase):

    def test_max_sum_circular_subarray(self):
        list_of_numbers = [8, -8, 9, -9, 10, -11, 12]
        self.assertEqual(find_maximum_sum_circular_subarray(list_of_numbers), 22)
        list_of_numbers = [10, -3, -4, 7, 6, 5, -4, -1]
        self.assertEqual(find_maximum_sum_circular_subarray(list_of_numbers), 23)
