import unittest
"""
Given an array with positive and negative numbers, find the maximum average subarray of given length.
Input: 1 12 -5 -6 50 3, k = 4
Output: 1 (12-5-6+50)/4
"""


def max_avg_subarray(list_of_numbers, k):
    assert len(list_of_numbers) >= k

    cur_max = sum(list_of_numbers[0:k])
    cur_max_index = 0
    j = 0
    for i in range(k, len(list_of_numbers)):
        cur_sum = cur_max - list_of_numbers[j] + list_of_numbers[i]
        if cur_sum > cur_max:
            cur_max = cur_sum
            cur_max_index = j+1
        j += 1

    return cur_max_index


class TestMaxAvgSubarray(unittest.TestCase):

    def test_max_avg_subarray(self):
        list_of_numbers = [1, 12, -5, -6, 50, 3]
        self.assertEqual(max_avg_subarray(list_of_numbers, 4), 1)

