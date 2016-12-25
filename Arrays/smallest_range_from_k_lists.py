import unittest
import heapq
"""
Given k sorted lists of integers of size n each, find the smallest range than includes
at least one element from each of the k lists. If more than one smallest range exists, return any of
them.
Input:
arr1: 4 7 9 12 15
arr2: 0 8 10 14 20
arr3: 6 12 16 30 50
Output: 6-8
"""

"""
Approach:
1. The idea is to use a min heap.
2. First, create the min heap using first element of each of the k lists.
3. Find the minimum (root of heap) and maximum elements among them and compute the range.
4. Next, insert the next element from the list containing the current heap and recompute min, max and range if
    needed.
5. Break if any of the lists becomes empty of range has consecutive elements.
"""


def smallest_range_from_k_lists(k_lists):
    best_range = float('inf')
    smallest_range = None

    min_heap = []

    for index, list_of_ints in enumerate(k_lists):
        entry = [list_of_ints[0], index]
        heapq.heappush(min_heap, entry)

    max_val = max([list_of_ints[0] for list_of_ints in k_lists])

    while True:
        min_val, list_index = heapq.heappop(min_heap)
        if max_val - min_val + 1 < best_range:
            best_range = max_val - min_val + 1
            smallest_range = min_val, max_val
            if best_range + 1 == len(k_lists):
                break
        k_lists[list_index].remove(min_val)
        if len(k_lists[list_index]) > 0:
            next_val = k_lists[list_index][0]
            if next_val > max_val:
                max_val = next_val
            entry = [next_val, list_index]
            heapq.heappush(min_heap, entry)
        else:
            break

    return smallest_range


class TestSmallestRange(unittest.TestCase):

    def test_smallest_range(self):
        k_lists = [[4, 7, 9, 12, 15], [0, 8, 10, 14, 20], [6, 12, 16, 30, 50]]
        self.assertEqual(smallest_range_from_k_lists(k_lists), (6, 8))
        k_lists = [[4, 7, 30], [1, 2], [20, 40]]
        self.assertEqual(smallest_range_from_k_lists(k_lists), (2, 20))
