import unittest
"""
Given an array of integers, return an index i such that sum(A[0..i-1]) == sum(A[i+1...n-1]).
Input: -7 1 5 2 -4 3 0
Output: 3
"""

"""
DAMN!
Approach:
1. Compute the sum of the array first, total_sum
2. Scan from left to right.
3. Initialize leftSum to zero.
4. leftSum = leftSum + arr[i]
5. rightSum = sum - arr[i]
6. If leftSum == rightSum, return i.
"""


def find_equilibrium_index(list_of_numbers):

    total_sum = sum(list_of_numbers)
    left_sum = 0

    for i in range(len(list_of_numbers)):
        total_sum = total_sum - list_of_numbers[i]
        if left_sum == total_sum:
            return i
        left_sum += list_of_numbers[i]

    return -1


class TestEquilibriumIndex(unittest.TestCase):

    def test_equilibrium_index(self):
        list_of_numbers = [-7, 1, 5, 2, -4, 3, 0]
        self.assertEqual(find_equilibrium_index(list_of_numbers), 3)


if __name__ == '__main__':
    unittest.main()
