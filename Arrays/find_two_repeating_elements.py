import unittest
"""
Given an array of n+2 elements, all elements of the array are in the range 1 to n. All elements
occur once except two elements which occur twice. Find the two repeating numbers.
Input: 4 2 4 5 2 3 1, n = 5
Output: 4 2
"""


def find_two_repeating(list_of_numbers):
    max_possible = len(list_of_numbers) - 2
    repeating_numbers = []

    for index in range(max_possible + 1):
        val = abs(list_of_numbers[index])
        if list_of_numbers[val] < 0:
            repeating_numbers.append(val)
        list_of_numbers[val] = -list_of_numbers[val]

    return repeating_numbers


class TestRepeating(unittest.TestCase):

    def test_two_repeating(self):
        list_of_numbers = [4, 2, 4, 5, 2, 3, 1]
        repeating = find_two_repeating(list_of_numbers)
        self.assertEqual(len(repeating), 2)
        self.assertIn(4, repeating)
        self.assertIn(2, repeating)

