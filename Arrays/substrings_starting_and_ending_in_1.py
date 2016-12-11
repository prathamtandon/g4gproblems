import unittest
"""
Given a binary string, count the number of substrings starting and ending in 1.
Input: 00100101
Output: 3 (100101, 1001, 101)
"""

"""
Approach:
Damn! Nice trick.
1. Count the number of 1s in the string. Let this be m.
2. Return m(m-1)/2.
3. That's nothing but C(m,2). That is all possible pairs of 1s in the string. Each pair corresponds to
starting and ending of a substring.
"""


def count_substrings_starting_and_ending_in_1(binary_string):

    count_of_1s = binary_string.count(1)
    return count_of_1s * (count_of_1s - 1) / 2


class TestCountSubstrings(unittest.TestCase):

    def test_count_substrings(self):
        binary_string = [1, 0, 0, 1, 0, 0, 1, 1, 0, 0]
        self.assertEqual(count_substrings_starting_and_ending_in_1(binary_string), 6)
