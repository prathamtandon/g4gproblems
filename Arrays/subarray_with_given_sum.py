import unittest
"""
Given an unsorted array of positive integers, find a contiguous subarray
which adds to a given number.
Input: 1 4 20 3 10 5, sum = 33
Output: Sum between indices 2 and 4.
Input: 1 4, sum = 0
Output: No subarray
"""

"""
Approach:
1. Have two pointers, start and end.
2. Keep moving end forward, and keep a running sum.
3. When sum > desired sum, move start forward and keep removing from sum until sum becomes less than sum.
4. Return start and end when running sum becomes equal to desired sum.
NOTE: Its important to understand how the indices work. Start always points to start of subarray.
End, however, points to element after the end of subarray. That's the reason, we return start, end-1.
Also, inner while loop checks that start should not equal current end of subarray, which is actually end-1.
This is needed to ensure the third test case listed below passes.
"""


def find_subarray_with_given_sum(list_of_numbers, sum):
    running_sum = list_of_numbers[0]
    start = 0

    for end in range(1, len(list_of_numbers)+1):
        while start < end-1 and running_sum > sum:
            running_sum -= list_of_numbers[start]
            start += 1
        if running_sum == sum:
            return start, end-1
        if end < len(list_of_numbers):
            running_sum += list_of_numbers[end]
    return None


def find_subarray_with_given_sum_general(list_of_numbers, sum):
    """
    Note that list of numbers can contain negative numbers also.
    """
    map = {}
    running_sum = 0
    for i in xrange(len(list_of_numbers)):
        running_sum += list_of_numbers[i]
        if running_sum == sum:
            print 'Found sum at: ' + str(0) + ',' + str(i)
            return
        if running_sum - sum in map:
            print 'Found sum at: ' + str(map[running_sum - sum] + 1) + ',' + str(i)
            return
        map[running_sum] = i

    print 'Sum not found'


class TestSubarraySum(unittest.TestCase):

    def test_subarray_with_given_sum(self):
        list_of_numbers = [1, 4, 20, 3, 10, 5]
        self.assertEqual(find_subarray_with_given_sum(list_of_numbers, 33), (2, 4))
        list_of_numbers = [15, 2, 4, 8, 9, 5, 10, 23]
        self.assertEqual(find_subarray_with_given_sum(list_of_numbers, 23), (1, 4))
        list_of_numbers = [1, 4]
        self.assertIsNone(find_subarray_with_given_sum(list_of_numbers, 0))

    def test_subarray_general(self):
        list_of_numbers = [10, 2, -2, -20, 10]
        find_subarray_with_given_sum_general(list_of_numbers, -10)
