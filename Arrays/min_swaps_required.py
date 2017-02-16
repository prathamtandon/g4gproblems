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

"""
Approach:
1. Start scanning from left to right.
2. If first and second, already form a pair, then recur for the remaining list of numbers.
3. Else return the minimum of following two cases:
    a. Recur after swapping first with element that forms pair with second.
    b. Recur after swapping second with element that forms pair with first.
"""


def min_swaps_required(list_of_numbers, list_of_pairs):
    return min_swaps_required_helper(list_of_numbers, list_of_pairs, 0)


def forms_pair(ele1, ele2, list_of_pairs):
    for pair in list_of_pairs:
        if pair[0] == ele1 and pair[1] == ele2 or pair[0] == ele1 and pair[1] == ele2:
            return True
    return False


def swap_in_list(list_of_numbers, start_index, one_from_pair, dest_index, list_of_pairs):
    second_from_pair = 0
    for pair in list_of_pairs:
        if pair[0] == one_from_pair:
            second_from_pair = pair[1]
        elif pair[1] == one_from_pair:
            second_from_pair = pair[0]
    found = -1
    for i in range(start_index, len(list_of_numbers)):
        if list_of_numbers[i] == second_from_pair:
            found = i
            break
    list_of_numbers[found], list_of_numbers[dest_index] = list_of_numbers[dest_index], list_of_numbers[found]
    return list_of_numbers


def min_swaps_required_helper(list_of_numbers, list_of_pairs, index):
    if index >= len(list_of_numbers):
        return 0
    cur = list_of_numbers[index]
    next = list_of_numbers[index + 1]
    if forms_pair(cur, next, list_of_pairs):
        return min_swaps_required_helper(list_of_numbers, list_of_pairs, index + 2)
    else:
        list1 = swap_in_list(list_of_numbers[:], index+2, list_of_numbers[index], index+1, list_of_pairs)
        list2 = swap_in_list(list_of_numbers[:], index+2, list_of_numbers[index+1], index, list_of_pairs)
        return 1 + min(min_swaps_required_helper(list1, list_of_pairs, index + 2),
                       min_swaps_required_helper(list2, list_of_pairs, index + 2))


class TestMinSwaps(unittest.TestCase):

    def test_min_swaps(self):
        list_of_numbers = [3, 5, 6, 4, 1, 2]
        list_of_pairs = [(1, 3), (2, 6), (4, 5)]
        self.assertEqual(min_swaps_required(list_of_numbers, list_of_pairs), 2)
