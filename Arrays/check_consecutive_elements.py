import unittest
"""
Given an unsorted array of numbers, return true if the array only contains consecutive elements.
Input: 5 2 3 1 4
Ouput: True (consecutive elements from 1 through 5)
Input: 83 78 80 81 79 82
Output: True (consecutive elements from 78 through 83)
Input: 34 23 52 12 3
Output: False
"""

"""
Approach:
1. First check that there are (max - min + 1) elements in the array.
2. Second, check that all elements are unique.
3. If all elements are consecutive, we can use arr[i]-min as an index into the array.
4. If element is positive, make it negative, else if its negative, there is repetition.
NOTE: This only works if all numbers are positive, otherwise use a hashmap to check for dupes.
O(n) time complexity and O(1) space complexity.
"""


def check_consecutive_only(list_of_numbers):
    min_val = min(list_of_numbers)
    max_val = max(list_of_numbers)

    if len(list_of_numbers) != (max_val - min_val + 1):
        return False

    for num in list_of_numbers:
        index = abs(num) - min_val
        if list_of_numbers[index] < 0:
            return False
        list_of_numbers[index] = -list_of_numbers[index]

    return True


class TestConsecutiveElements(unittest.TestCase):

    def test_consecutive_true(self):
        list_of_numbers = [83, 78, 80, 81, 79, 82]
        self.assertTrue(check_consecutive_only(list_of_numbers))

    def test_consecutive_false(self):
        list_of_numbers = [7, 6, 5, 5, 3, 4]
        self.assertFalse(check_consecutive_only(list_of_numbers))
        list_of_numbers = [34, 23, 52, 12, 3]
        self.assertFalse(check_consecutive_only(list_of_numbers))
        list_of_numbers = [5, 2, 3, 3, 1]
        self.assertFalse(check_consecutive_only(list_of_numbers))
