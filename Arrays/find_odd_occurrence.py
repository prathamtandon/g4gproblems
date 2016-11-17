import unittest

"""
Given an array of positive integers, all numbers occur even number of times except one number
which occurs odd number of times. Find this number.
Input: 1 2 3 2 3 1 3
Output: 3
"""

"""
Approach:
A Bitwise XOR of all elements in the list gives us the odd occurring element.
"""


def get_odd_occurring(list_of_numbers):
    result = 0

    for num in list_of_numbers:
        result = result ^ num

    return result


class TestOddOccurring(unittest.TestCase):

    def test_odd_occurrence(self):
        list_of_numbers = [1, 2, 3, 2, 3, 1, 3]
        self.assertEqual(get_odd_occurring(list_of_numbers), 3)


if __name__ == '__main__':
    unittest.main()
