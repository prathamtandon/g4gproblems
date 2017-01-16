import unittest
"""
Count number of ways the person can climb up n stairs when person can climb up to m stairs at a time.
"""


def count_ways(n, m):

    ways = [0] * (n+1)
    ways[0] = 1
    ways[1] = 1

    for i in range(2, n+1):
        for j in range(1, m+1):
            if i-j >= 0:
                ways[i] += ways[i-j]

    return ways[n]


class TestCountWays(unittest.TestCase):

    def test_count_ways(self):
        self.assertEqual(count_ways(4, 2), 5)
