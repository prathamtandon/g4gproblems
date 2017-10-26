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
    ans = -1

    while low <= high:
        mid = (low + high) / 2
        if list_of_numbers[mid] >= ele:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


def find_longest_increasing_subsequence_length(list_of_numbers):
    LCS = [list_of_numbers[0]]

    for i in range(1, len(list_of_numbers)):
        cur_ele = list_of_numbers[i]
        k = find_ceil_index(LCS, cur_ele)
        if k == -1:
            LCS.append(cur_ele)
        else:
            LCS[k] = cur_ele

    return len(LCS)


class TestLIS(unittest.TestCase):

    def test_longest_increasing_subsequence(self):
        list_of_numbers = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
        self.assertEqual(find_longest_increasing_subsequence_length(list_of_numbers), 6)
        list_of_numbers = [2, 5, 3, 1, 2, 3, 4, 5, 6]
        self.assertEqual(find_longest_increasing_subsequence_length(list_of_numbers), 6)
        list_of_numbers = [5, 4, 3, 2, 1]
        self.assertEqual(find_longest_increasing_subsequence_length(list_of_numbers), 1)

