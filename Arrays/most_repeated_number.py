import unittest
"""
Given an array of size n, where each number is between 0 and k-1 where k is a positive integer and k <= n.
Find the most repeating number in time complexity O(n) and space complexity O(1). You can modify the original
array.
Input: 2 3 3 5 3 4 1 7, k = 8, n = 8
Output: 3
"""

"""
Approach:
1. Scan the list from left to right.
2. For each arr[i], increment arr[arr[i]%k] by k.
3. The most repeating number is the index of the maximum value present in the array.
4. By doing %k, we are ensuring we get back the original value. This is because (p+m*k)%k = p%k
"""


def most_repeated_number(list_of_numbers, k):

    for i in range(len(list_of_numbers)):
        target_index = list_of_numbers[i] % k
        list_of_numbers[target_index] += k

    return list_of_numbers.index(max(list_of_numbers))


class TestMostRepeating(unittest.TestCase):

    def test_most_repeating(self):
        self.assertEqual(most_repeated_number([2, 3, 3, 5, 3, 4, 1, 7], 8), 3)


