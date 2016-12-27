import unittest
"""
Given an array, find the number of subarrays with even sum.
Input: 1 2 2 3 4 1
Output: 9
"""

"""
Approach:
1. If temp[i] is the cumulative sum of the array from arr[0...i], arr[i...j] is even sum subarray if
    temp[j]-temp[i] % 2 = 0.
2. So, we keep a running sum modulo 2 and count how many times the value is zero or one.
3. Value is zero for even sum and 1 for odd sum.
4. Since, a+b is even if both a and b are odd or both are even, temp[j]-temp[i] is even if both temp[j]
and temp[i] are even or both are odd.
5. So, we just have to chose two indices from the temp array: C(n,2) = n*(n-1)/2
"""


def subarrays_with_even_sum(list_of_nums):

    sum_count = [1, 0]  # sum[0] is even count and sum[1] is odd counts
    sum_val = 0

    for i in range(len(list_of_nums)):
        sum_val = ((sum_val + list_of_nums[i] % 2) + 2) % 2  # plus 2 is to handle odd values
        sum_count[sum_val] += 1

    return sum_count[0] * (sum_count[0] - 1) / 2 + sum_count[1] * (sum_count[1] - 1) / 2


class TestSubarrayEvenSum(unittest.TestCase):

    def test_subarray_even_sum(self):
        list_of_nums = [1, 2, 2, 3, 4, 1]
        self.assertEqual(subarrays_with_even_sum(list_of_nums), 9)
