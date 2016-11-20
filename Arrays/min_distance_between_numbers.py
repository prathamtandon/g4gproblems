import unittest
"""
Given an array of numbers, find the minimum distance between two given numbers x and y.
There may be duplicates in the list. Assume that x and y are present in the list.
Input: 1 2, x = 1 y = 2
Output: 1
Input: 3 4 5, x = 3 y = 5
Output: 2
Input: 2 5 3 5 4 4 2 3, x = 3 y = 2
Output: 1
"""

"""
Approach:
1. Keep track of two variables, x_last_seen and y_last_seen.
2. Whenever one gets updated, compute the new difference can compare with current minimum.
3. Return the minimum found this way.
"""


def min_distance_x_and_y(list_of_numbers, x, y):
    x_last_seen = -1
    y_last_seen = -1

    min_distance = len(list_of_numbers) + 1

    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] == x:
            x_last_seen = i
            if y_last_seen != -1:
                min_distance = min(min_distance, abs(y_last_seen - x_last_seen))
        elif list_of_numbers[i] == y:
            y_last_seen = i
            if x_last_seen != -1:
                min_distance = min(min_distance, abs(y_last_seen - x_last_seen))

    return min_distance


class TestMinDistance(unittest.TestCase):

    def test_min_distance_x_and_y(self):
        list_of_numbers = [2, 5, 3, 5, 4, 4, 2, 3]
        self.assertEqual(min_distance_x_and_y(list_of_numbers, 2, 3), 1)
