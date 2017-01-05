"""
Given an array of integers where each element represents the max number of steps
that can be made forward from that element. Write a function to return the minimum number
of jumps to reach the end of the array (starting from the first element).
"""
import unittest


def min_jumps_to_reach_end(jumps):
    end = len(jumps)
    # Let costs[i] define the min jumps needed from arr[i] to last element.
    costs = [float('inf') for _ in range(end)]
    last_index = end-1
    costs[last_index] = 0

    for i in range(last_index-1, -1, -1):
        for j in range(jumps[i]):
            if i+j+1 <= last_index:
                costs[i] = min(costs[i], costs[i+j+1])
            else:
                break
        costs[i] += 1

    return costs[0]


class TestMinJumps(unittest.TestCase):

    def test_min_jumps(self):
        jumps = [1, 3, 6, 1, 0, 9]
        self.assertEqual(min_jumps_to_reach_end(jumps), 3)
