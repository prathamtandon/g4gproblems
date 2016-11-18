import unittest
"""
Given an array of positive integers, find the maximum sum of a sub-sequence with the
constraint that no two numbers in the sequence should be adjacent in the array.
Input: 3 2 7 10
Output: 13 (3 + 10)
Input 3 2 5 10 7
Output: 15 (3 + 5 + 7)
"""

"""
Approach:
1. Similar to 0-1 Knapsack problem.
2. F(S,i) = max(S[i] + F(S,i+2), F(S,i+1))
3. That is, for every element either include it, in which case remaining elements start from 2 positions away
    else exclude it, in which case remaining elements start from 1 position away.
"""

"""
Approach:
1. This one uses just 2 variables.
2. First variable tracks the maximum sum obtained by excluding current element
3. Second variable is current element added to first variable
4. Return max(first variable, second variable)
"""


def max_sum_not_adjacent_helper(list_of_numbers, index):
    if index >= len(list_of_numbers):
        return 0
    return max(list_of_numbers[index] + max_sum_not_adjacent_helper(list_of_numbers, index+2),
               max_sum_not_adjacent_helper(list_of_numbers, index+1))


def max_sum_not_adjacent(list_of_numbers):
    return max_sum_not_adjacent_helper(list_of_numbers, 0)


def max_sum_not_adjacent_iterative(list_of_numbers):
    sum_including_current = 0
    sum_excluding_current = 0

    for number in list_of_numbers:
        new_sum_excluding_current = max(sum_including_current, sum_excluding_current)
        sum_including_current = sum_excluding_current + number
        sum_excluding_current = new_sum_excluding_current

    return max(sum_including_current, sum_excluding_current)


class TestMaxSumNotAdjacent(unittest.TestCase):

    def test_max_sum_not_adjacent(self):
        list_of_numbers = [3, 2, 7, 10]
        self.assertEqual(max_sum_not_adjacent(list_of_numbers), 13)
        list_of_numbers = [3, 2, 5, 10, 7]
        self.assertEqual(max_sum_not_adjacent(list_of_numbers), 15)
        list_of_numbers = [5, 5, 10, 40, 50, 35]
        self.assertEqual(max_sum_not_adjacent(list_of_numbers), 80)

    def test_max_sum_not_adjacent_iterative(self):
        list_of_numbers = [3, 2, 7, 10]
        self.assertEqual(max_sum_not_adjacent_iterative(list_of_numbers), 13)
        list_of_numbers = [3, 2, 5, 10, 7]
        self.assertEqual(max_sum_not_adjacent_iterative(list_of_numbers), 15)
        list_of_numbers = [5, 5, 10, 40, 50, 35]
        self.assertEqual(max_sum_not_adjacent_iterative(list_of_numbers), 80)
