"""
Given an array of integers where each element represents the max number of steps
that can be made forward from that element. Write a function to return the minimum number
of jumps to reach the end of the array (starting from the first element).
"""
import unittest


def min_jumps_to_reach_end(jumps):
    n = len(jumps)
    # Let costs[i] define the min jumps needed to reach arr[i] from start of array.
    costs = [float('inf') for _ in range(n)]
    costs[0] = 0

    for i in range(1, n):
        for j in range(i):
            if jumps[j] >= i-j:
                costs[i] = min(costs[i], costs[j])
        costs[i] += 1

    return costs[n-1]


class TestMinJumps(unittest.TestCase):

    def test_min_jumps(self):
        jumps = [1, 3, 6, 1, 0, 9]
        self.assertEqual(min_jumps_to_reach_end(jumps), 3)
