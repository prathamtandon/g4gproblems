import unittest
"""
Given an unsorted array of numbers, and a value, find a triplet whose sum is equal to value.
Input: 12 3 4 1 6 9, value = 24
Output: 12 3 9
"""

"""
Approach:
1. Sort the array.
2. Scan from left to right.
3. Fix current element as potential first element of triplet.
4. Find a pair which has sum as value - current element in the remaining sorted portion of array.
"""


def find_triplet_with_given_sum(list_of_numbers, target_sum):
    list_of_numbers = sorted(list_of_numbers)
    for i in range(len(list_of_numbers)):
        low = i+1
        high = len(list_of_numbers)-1
        while low < high:
            actual_sum = list_of_numbers[i] + list_of_numbers[low] + list_of_numbers[high]
            if actual_sum == target_sum:
                return list_of_numbers[i], list_of_numbers[low], list_of_numbers[high]
            elif actual_sum < target_sum:
                low += 1
            else:
                high -= 1
    return None


class TestTripletSum(unittest.TestCase):

    def test_triplet_sum(self):
        list_of_numbers = [12, 3, 4, 1, 6, 9]
        triplet = find_triplet_with_given_sum(list_of_numbers, 24)
        self.assertEqual(len(triplet), 3)
        self.assertIn(12, triplet)
        self.assertIn(3, triplet)
        self.assertIn(9, triplet)
        self.assertIsNone(find_triplet_with_given_sum(list_of_numbers, -12))
