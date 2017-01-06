import unittest
"""
Given n eggs and k floors, find minimum number of drops needed to determine critical floor.
Critical floor is a floor such that all eggs will break if dropped from critical floor or above, but
will not break if dropped from below critical floor.
"""

"""
Approach:
We will try out by dropping starting at all floors from 1, 2,... up to k.
If egg is dropped from floor k, it will either break or it will not break. If it breaks,
we need to check from floors 1,2,...,k-1. If it does not break, we need to check from floors
k+1,k+2,...last floor. This can be written as following recursive equation:
egg_drop[n][k] = 1 + min(max(egg_drop[n-1][x-1], egg_drop[n][k-x]) for x in [1,2,...,k])
"""


def egg_drop(num_eggs, num_floors):
    table = [[float('inf')] * (num_floors + 1) for _ in range(num_eggs + 1)]

    #  We need 1 drop for 1st floor and 0 drops for 0 floors
    for i in range(1, num_eggs + 1):
        table[i][1] = 1
        table[i][0] = 0

    # If there is only one egg, it must be dropped from all floors
    for i in range(1, num_floors + 1):
        table[1][i] = i

    for i in range(2, num_eggs + 1):
        for j in range(2, num_floors + 1):
            for x in range(1, j+1):
                table[i][j] = min(table[i][j], 1 + max(table[i-1][x-1], table[i][j-x]))

    return table[num_eggs][num_floors]


class TestEggDrop(unittest.TestCase):

    def test_egg_drop(self):
        num_floors = 36
        num_eggs = 2
        self.assertEqual(egg_drop(num_eggs, num_floors), 8)
