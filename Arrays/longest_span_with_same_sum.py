import unittest
"""
Given two binary arrays arr1[] and arr2[] of same size n, find the length of longest common span (i, j)
where j >= i such that arr1[i] + arr1[i+1] + ... + arr1[j] = arr2[i] + arr2[i+1] + ... + arr2[j].
Input: arr1[]: 0 1 0 0 0 0
       arr2[]: 1 0 1 0 0 1
Output: 4
The longest span is from index 1 to 4.
"""

"""
Approach:
1. We find the prefix sums in the two arrays and calculate their difference.
2. Consider the start and end of any span with same sum.
3. The difference of prefix sums at start and end will be the same. This is because the span has same
   sum in both the arrays and hence, does not change the difference from start to end.
4. Since both binary arrays are of same length, difference in sums can vary from -n to n ie 2n+1 values.
5. If prefix difference is zero, then max_length is current_index+1 # span goes from 0 to current_index+1
6. If prefix difference is encountered for first time, we store the current_index.
7. If prefix difference is encountered before, we compute difference between stored value and current_index.
"""


def longest_span_with_same_sum(first_bin_array, second_bin_array):

    assert len(first_bin_array) == len(second_bin_array)
    end = len(first_bin_array)
    difference_list = [-1] * (2*end + 1)
    first_prefix_sum = 0
    second_prefix_sum = 0
    max_length = 0

    for j in range(end):
        first_prefix_sum += first_bin_array[j]
        second_prefix_sum += second_bin_array[j]
        difference = first_prefix_sum - second_prefix_sum
        if difference == 0:
            max_length = j+1
        if difference_list[difference] == -1:
            difference_list[difference] = j
        else:
            i = difference_list[difference]
            if j-i > max_length:
                max_length = j-i

    return max_length


class TestLongestSpan(unittest.TestCase):

    def test_longest_span(self):
        first_bin_array = [0, 1, 0, 1, 1, 1, 1]
        second_bin_array = [1, 1, 1, 1, 1, 0, 1]
        self.assertEqual(longest_span_with_same_sum(first_bin_array, second_bin_array), 6)
        first_bin_array = [0, 0, 1, 0]
        second_bin_array = [1, 1, 1, 1]
        self.assertEqual(longest_span_with_same_sum(first_bin_array, second_bin_array), 1)
