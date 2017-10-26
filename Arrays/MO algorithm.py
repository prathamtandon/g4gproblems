from math import sqrt
import unittest
"""
We have an array arr[0 . . . n-1], where each element <= n. We should be able to efficiently find the all values
from index L (query start) to R (query end) where 0 <= L <= R <= n-1 which occur at least 3 times
in arr[L...R]
Input:  arr[]   = {1, 2, 3, 1, 1, 2, 1, 2, 3, 1};
        query[] = [0, 4], [1, 8]

Output: Minimum of [0, 4] is 1
        Minimum of [1, 8] is 2
"""

"""
Approach:
1. A naive way is to loop through all ranges, and find the count of all elements in that range. Runtime complexity
   is O(M*N) where M is number of ranges and N is number of elements.
2. We can get O((M+N)*SQRT(N)) runtime using MO's algorithm.
3. The idea is to divide array into blocks, each of size SQRT(N). So, there will be SQRT(N) such blocks.
4. To find elements in given range, we use information from previous range.
5. First, we pre-process all the ranges so that they are sorted on their L(left) values first. That is,
   all ranges with 0 <= L <= SQRT(N)-1 will go to first block, SQRT(N) <= L <= 2*SQRT(N)-1 to second block,
   and so on.
6. Within a block, ranges are sorted on R(right) values in ascending order.
7. We use, currentL and currentR to denote left and right values of range just processed.
8. We use L and R to denote left and right values of range we have to process next.
9. By moving currentL and currentR pointers appropriately, we can modify the answer from previous range to obtain
   answer for current range.
10. Let's analyze runtime complexity of this algorithm. The currentR pointer can move O(N) times within a block.
   Since, there are SQRT(N) blocks, right pointer moves a total O(N*SQRT(N)) times.
11. The currentL pointer will only move within a block, size of the block times. Size of each block is SQRT(N).
   If Q queries fall in a given block, total movement in that block will be O(Q*SQRT(N)). Overall, there are
   M queries, so total movement across all blocks is O(M*SQRT(N)).
12. Total runtime of algorithm is sum of movements of both pointers, which is O((M+N)*SQRT(N)).
"""


class Range:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class MinimumOccurrence:

    def __init__(self, arr, ranges, threshold):
        self.arr = arr
        self.block_size = sqrt(len(self.arr))
        self.ranges = self.convert_to_ranges(ranges)
        self.threshold = threshold
        self.count = [0] * len(self.arr)
        self.answers = []
        self.running_count = 0

    def increment_occurrence(self, index):
        self.count[self.arr[index]] += 1
        if self.count[self.arr[index]] == self.threshold:
            self.running_count += 1

    def decrement_occurrence(self, index):
        self.count[self.arr[index]] -= 1
        if self.count[self.arr[index]] == self.threshold - 1:
            self.running_count -= 1

    def convert_to_ranges(self, ranges):
        result = []
        for i in range(len(ranges)):
            result.append(Range(ranges[i][0], ranges[i][1]))
        return result

    def range_comparator(self, first, second):
        first_block = first.left / self.block_size
        second_block = second.left / self.block_size
        if first_block != second_block:
            # sort on block first
            return first_block < second_block
        return first.right < second.right

    def count_ranges(self):
        self.ranges = sorted(self.ranges, cmp=self.range_comparator)
        current_l = 0
        current_r = 0

        for i in range(len(self.ranges)):
            l = self.ranges[i].left
            r = self.ranges[i].right

            while current_l < l:
                self.decrement_occurrence(current_l)
                current_l += 1

            while current_l > l:
                self.increment_occurrence(current_l-1)
                current_l -= 1

            while current_r <= r:
                self.increment_occurrence(current_r)
                current_r += 1

            while current_r > r+1:
                self.decrement_occurrence(current_r-1)
                current_r -= 1

            self.answers.append(self.running_count)

        return self.answers


class TestMOAlgorithm(unittest.TestCase):

    def test_min_occurrences(self):
        arr = [1, 2, 3, 1, 1, 2, 1, 2, 3, 1]
        ranges = [(0, 4), (1, 8), (0, 9)]
        object = MinimumOccurrence(arr, ranges, 3)
        self.assertEqual(object.count_ranges(), [1, 2, 2])

