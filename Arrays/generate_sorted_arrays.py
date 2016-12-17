import unittest
"""
Given two sorted arrays A and B, generate all possible arrays such that first element is taken
from A then from B then from A and so on in increasing order till the arrays are exhausted. The generated
arrays should end in an element from B.
Input:
A: 10 15 25
B: 1 5 20 30
Output:
10 20
10 20 25 30
10 30
15 20
15 20 25 30
15 30
25 30
"""

"""
Approach:
1. Scan A from left to right.
2. Scan B from left to right until B[j] > A[i].
3. Start a new recursion with this state, in each successive call, flip the active list (ie the list from which
    next element is to be selected).
"""


def generate_sorted_arrays(first_sorted, second_sorted):
    result = []
    for i in range(len(first_sorted)):
        for j in range(len(second_sorted)):
            if first_sorted[i] < second_sorted[j]:
                generate_sorted_arrays_helper(first_sorted, second_sorted, True, i, j, [first_sorted[i]], result)

    return result


def generate_sorted_arrays_helper(first_sorted, second_sorted, is_first_active, first_index, second_index, so_far,
                                   result):
    if first_index >= len(first_sorted) or second_index >= len(second_sorted):
        return
    end = len(so_far)
    to_compare = so_far[end - 1]
    if is_first_active:
        while second_index < len(second_sorted) and second_sorted[second_index] < to_compare:
            second_index += 1
        if second_index < len(second_sorted):
            so_far.append(second_sorted[second_index])
            result.append(so_far[:])
    else:
        while first_index < len(first_sorted) and first_sorted[first_index] < to_compare:
            first_index += 1
        if first_index < len(first_sorted):
            so_far.append(first_sorted[first_index])

    is_first_active = not is_first_active
    generate_sorted_arrays_helper(first_sorted,
                                  second_sorted,
                                  is_first_active,
                                  first_index,
                                  second_index,
                                  so_far,
                                  result)


class TestSortedArrays(unittest.TestCase):

    def test_sorted_arrays(self):
        first_sorted = [10, 15, 25]
        second_sorted = [1, 5, 20, 30]

        result = generate_sorted_arrays(first_sorted, second_sorted)

        self.assertEqual(len(result), 7)



