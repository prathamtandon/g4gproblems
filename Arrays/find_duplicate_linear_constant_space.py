import unittest
"""
You are given an array of integers of length n, where each element ranges
from 0 to n - 2, inclusive.  Prove that at least one  duplicate element must
exist, and give an O(n)-time, O(1)-space algorithm for finding some
duplicated element.  You must not modify the array elements during this
process.
"""

"""
Approach: http://keithschwarz.com/interesting/code/?dir=find-duplicate
"""


def find_duplicate_in_list(list_of_numbers):
    # We start at end of cycle and try to find an intersection point inside the cycle.
    slow = len(list_of_numbers) - 1
    fast = len(list_of_numbers) - 1

    # Keep advancing 'slow' by 1 step and 'fast' by 2 steps until they meet inside the cycle.
    while True:
        slow = list_of_numbers[slow]
        fast = list_of_numbers[list_of_numbers[fast]]
        if slow == fast:
            break

    # Start up another pointer at end of array and move it forward until it hits the
    # pointer inside the cycle.
    finder = len(list_of_numbers) - 1
    while True:
        finder = list_of_numbers[finder]
        slow = list_of_numbers[slow]

        # If the two hit, the intersection index is the duplicate element.
        if slow == finder:
            return slow


class TestFindDuplicate(unittest.TestCase):

    def test_find_duplicate_in_list(self):
        list_of_numbers = [1, 2, 2, 0]
        self.assertEqual(find_duplicate_in_list(list_of_numbers), 2)
        list_of_numbers = [2, 4, 3, 0, 1, 3]
        self.assertEqual(find_duplicate_in_list(list_of_numbers), 3)
        list_of_numbers = [3, 0, 0, 0]
        self.assertEqual(find_duplicate_in_list(list_of_numbers), 0)



