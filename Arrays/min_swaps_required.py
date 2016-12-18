import unittest
"""
There are n pairs and therefore 2n people. Everyone has a unique number ranging from 1 to 2n.
All these 2n persons arranged in random fashion in an array of size 2n. We are also given who is
partner of whom. Find the minimum number of swaps required to arrange these pairs such that all pairs
become adjacent to each other.
Input:
n = 3
pairs = 1,3 2,6 4,5
arr = 3 5 6 4 1 2

Output: 2
We can get 3 1 5 4 6 2 by swapping 5 & 6 and 6 & 1
"""


def min_swaps_required(list_of_numbers, list_of_pairs):
    return min_swaps_required_helper(list_of_numbers, list_of_pairs, 0, [])


def min_swaps_required_helper(list_of_numbers, list_of_pairs, swaps_so_far, swapped_indices):
    if len(list_of_pairs) == 0:
        return swaps_so_far
    list_of_pairs = list_of_pairs[:]
    cur_pair = list_of_pairs.pop(0)
    i = list_of_numbers.index(cur_pair[0])
    j = list_of_numbers.index(cur_pair[1])
    if abs(i - j) != 1:
        min_swaps = float('inf')
        if i-1 >= 0 and i-1 not in swapped_indices and j not in swapped_indices:
            temp = list_of_numbers[:]
            temp[i-1], temp[j] = temp[j], temp[i-1]
            swapped_indices = swapped_indices[:]
            swapped_indices.append(i-1)
            swapped_indices.append(i)
            min_swaps = min(min_swaps, min_swaps_required_helper(temp,
                                                                 list_of_pairs,
                                                                 swaps_so_far + 1,
                                                                 swapped_indices))
        if i+1 < len(list_of_numbers) and i+1 not in swapped_indices and j not in swapped_indices:
            temp = list_of_numbers[:]
            temp[i+1], temp[j] = temp[j], temp[i+1]
            swapped_indices = swapped_indices[:]
            swapped_indices.append(i+1)
            swapped_indices.append(i)
            min_swaps = min(min_swaps, min_swaps_required_helper(temp,
                                                                 list_of_pairs,
                                                                 swaps_so_far + 1,
                                                                 swapped_indices))
        if j-1 >= 0 and j-1 not in swapped_indices and i not in swapped_indices:
            temp = list_of_numbers[:]
            temp[j-1], temp[i] = temp[i], temp[j-1]
            swapped_indices = swapped_indices[:]
            swapped_indices.append(j)
            swapped_indices.append(j-1)
            min_swaps = min(min_swaps, min_swaps_required_helper(temp,
                                                                 list_of_pairs,
                                                                 swaps_so_far + 1,
                                                                 swapped_indices))
        if j+1 < len(list_of_numbers) and j+1 not in swapped_indices and i not in swapped_indices:
            temp = list_of_numbers[:]
            temp[j+1], temp[i] = temp[i], temp[j+1]
            swapped_indices = swapped_indices[:]
            swapped_indices.append(j)
            swapped_indices.append(j+1)
            min_swaps = min(min_swaps, min_swaps_required_helper(temp,
                                                                 list_of_pairs,
                                                                 swaps_so_far + 1,
                                                                 swapped_indices))
        return min_swaps
    else:
        return swaps_so_far


class TestMinSwaps(unittest.TestCase):

    def test_min_swaps(self):
        list_of_numbers = [3, 5, 6, 4, 1, 2]
        list_of_pairs = [(1, 3), (2, 6), (4, 5)]
        self.assertEqual(min_swaps_required(list_of_numbers, list_of_pairs), 2)
