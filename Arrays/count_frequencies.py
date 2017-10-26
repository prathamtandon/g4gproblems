import unittest
"""
Given an array of length n, where each value lies between 1 to n inclusive. Some values can be
repeated multiple times and some other values can be absent. Count frequency of all elements that are
present and print the missing elements. Expected time complexity is O(n) and expected space complexity is O(1).
Input: 2 3 3 2 5
Output: 1 => 0
        2 => 2
        3 => 2
        4 => 0
        5 => 1
"""


"""
Approach:
1. Idea is to store the frequency of an index i at arr[i].
2. This is achieved by doing arr[i] = arr[arr[i]%n] + n.
3. We need to do some index manipulations as the range of values is from 1 to n and indices go from 0 to n-1.
"""


def count_frequencies(list_of_numbers):

    end = len(list_of_numbers)
    divisor = end + 1
    for i in range(end):
        index = (list_of_numbers[i] % divisor) - 1
        list_of_numbers[index] += divisor

    counts = [x / divisor for x in list_of_numbers]
    return counts


class TestCountFrequencies(unittest.TestCase):

    def test_count_frequencies(self):
        list_of_numbers = [2, 3, 3, 2, 5]
        self.assertEqual(count_frequencies(list_of_numbers), [0, 2, 2, 0, 1])
        list_of_numbers = [4, 4, 4, 4]
        self.assertEqual(count_frequencies(list_of_numbers), [0, 0, 0, 4])
