import unittest
"""
Given an unordered array of integers, find the length of longest increasing subsequence.
Input: 0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15
Output: 6 (0, 2, 6, 9, 11, 15)
"""

"""
A great explanation of the approach appears here:
http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
"""


def find_ceil_index(list_of_numbers, ele):
    """
    Returns the smallest element in list_of_numbers greater than or equal to ele.
    """
    low = 0
    high = len(list_of_numbers)-1

    while high > low:
        mid = low + (high - low) / 2
        if list_of_numbers[mid] < ele:
            low = mid + 1
        else:
            high = mid

    return high


def find_longest_increasing_subsequence_length(list_of_numbers):
    tail_list = [0] * len(list_of_numbers)
    tail_list[0] = list_of_numbers[0]
    longest_length = 1

    for i in range(1, len(list_of_numbers)):
        cur_ele = list_of_numbers[i]
        if cur_ele < tail_list[0]:
            tail_list[0] = cur_ele  # Case 1: Create a new active list
        elif cur_ele > tail_list[longest_length-1]:
            tail_list[longest_length] = cur_ele  # Case 2: Clone and extend
            longest_length += 1
        else:
            smallest_index_bigger_than_cur = \
                find_ceil_index(tail_list[:longest_length], cur_ele)  # Case 3: Clone, extend and discard
            tail_list[smallest_index_bigger_than_cur] = cur_ele

    return longest_length


class TestLIS(unittest.TestCase):

    def test_longest_increasing_subsequence(self):
        list_of_numbers = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        self.assertEqual(find_longest_increasing_subsequence_length(list_of_numbers), 6)
        list_of_numbers = [2, 5, 3, 1, 2, 3, 4, 5, 6]
        self.assertEqual(find_longest_increasing_subsequence_length(list_of_numbers), 6)
        list_of_numbers = [5, 4, 3, 2, 1]
        self.assertEqual(find_longest_increasing_subsequence_length(list_of_numbers), 1)

