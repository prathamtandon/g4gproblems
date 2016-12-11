import unittest
"""
Given an array of integers, returns True if there is a triplet (a, b, c) that satisfies c^2 = a^2 + b^2.
Input: 3 1 4 6 5
Output: True (3 4 5)
Input: 10 4 6 12 5
Output: False
"""

"""
Approach:
1. Find the square of all items.
2. Sort the array in non-decreasing order.
3. Fix c as last element of array. Find if there is a pair of elements in remaining array which sum to c.
4. If such pair is found, return True. Else set c as next element from end.
"""


def pythagorean_triplet(list_of_numbers):

    list_of_numbers = [x**2 for x in list_of_numbers]
    list_of_numbers = sorted(list_of_numbers)
    end = len(list_of_numbers)

    for j in range(end-1, 2, -1):
        left = 0
        right = j - 1
        while left < right:
            pair = list_of_numbers[left] + list_of_numbers[right]
            if pair == list_of_numbers[j]:
                return True
            elif pair < list_of_numbers[j]:
                left += 1
            else:
                right -= 1

    return False


class TestPythagoreanTriplet(unittest.TestCase):

    def test_pythagorean_triplet(self):
        list_of_numbers = [3, 1, 4, 6, 5]
        self.assertTrue(pythagorean_triplet(list_of_numbers))
        list_of_numbers = [10, 4, 6, 12, 5]
        self.assertFalse(pythagorean_triplet(list_of_numbers))
