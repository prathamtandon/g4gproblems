import unittest
"""
Given an array of integers, find all combination of four elements in the array whose sum
is equal to a given value X.
Input: 10 2 3 4 5 9 7 8, X = 23
Output: 2 3  10 8
Input: -3 4 112 -1 5 0 5, X = 8
Output: 4 -1 5 0
"""

"""
Approach 1:
1. Sort the array.
2. Run outermost loop which fixes the first element.
3. Run inner loop which fixes the second element.
4. Find a pair in remaining (sorted) array that sums to X-first-second in linear time.
5. Overall time complexity is O(n^3).
"""

"""
Approach 2:
1. Pre-compute the sum of all pair of elements in the array. Store this in an auxiliary array.
2. For each element in auxiliary array, we can find the other pair in logN time using binary search.
3. Now, once we have the two pairs, we can return the corresponding elements as the solution.
"""


def binary_search(list_of_numbers, low, high, key):

    while low < high:
        mid = low + (high - low) / 2
        if list_of_numbers[mid] == key:
            return mid
        elif list_of_numbers[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


class PairSum:
    def __init__(self, first, second, pair_sum):
        self.first = first
        self.second = second
        self.pair_sum = pair_sum

    def __cmp__(self, other):
        cmp_val = self.pair_sum - other.pair_sum
        if cmp_val == 0:
            return 0
        if cmp_val < 0:
            return -1
        return 1

    def __eq__(self, other):
        return self.pair_sum == other.pair_sum


def find_four_numbers_that_sum_to_given_val(list_of_numbers, desired_sum):
    pair_sums = []

    for i in range(len(list_of_numbers)-1):
        for j in range(i+1, len(list_of_numbers)):
            new_pair = PairSum(i, j, list_of_numbers[i] + list_of_numbers[j])
            pair_sums.append(new_pair)

    pair_sums = sorted(pair_sums)

    for i in range(len(pair_sums)-1):
        left_pair_sum = pair_sums[i].pair_sum
        right_pair_sum = desired_sum - left_pair_sum
        k = pair_sums[i].first
        l = pair_sums[i].second
        pair_sums_copy = pair_sums[:]
        pair_sums_copy.pop(i)
        j = binary_search([x.pair_sum for x in pair_sums_copy], 0, len(pair_sums_copy)-1, right_pair_sum)
        if j >= 0 and pair_sums_copy[j].first not in [k, l] and pair_sums_copy[j].second not in [k, l]:
            return list_of_numbers[k], \
                   list_of_numbers[l], \
                   list_of_numbers[pair_sums_copy[j].first], \
                   list_of_numbers[pair_sums_copy[j].second]

    return None


class TestQuadrupleWithGivenSum(unittest.TestCase):

    def test_quadruple_with_given_sum(self):
        list_of_numbers = [10, 2, 3, 4, 5, 9, 7, 8]
        desired_sum = 23
        result = find_four_numbers_that_sum_to_given_val(list_of_numbers, desired_sum)
        self.assertEqual(len(result), 4)
        self.assertIn(3, result)
        self.assertIn(2, result)
        self.assertIn(10, result)
        self.assertIn(8, result)

        list_of_numbers = [-3, 4, 112, -1, 5, 0, 5]
        desired_sum = 8
        result = find_four_numbers_that_sum_to_given_val(list_of_numbers, desired_sum)
        self.assertEqual(len(result), 4)
        self.assertIn(4, result)
        self.assertIn(-1, result)
        self.assertIn(5, result)
        self.assertIn(0, result)
