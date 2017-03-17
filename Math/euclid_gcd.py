import unittest
"""
Find GCD of two numbers using Euclid's algorithm.
Input: 2336, 1314
Output: 146
"""

"""
Approach:
1. The idea is to express the larger number as the multiple of the smaller number plus some remainder.
2. Next we repeat the process by using the smaller number and the remainder ie express the smaller
   number as multiple of remainder plus a new remainder and so on.
3. We continue until we remainder becomes zero.
NOTE: The product of two numbers = The product of their GCD and their LCM.
"""


class GCD:
    def __init__(self, first, second):
        self.first = max(first, second)
        self.second = min(first, second)

    def euclid(self):
        return self.euclid_recursive(self.first, self.second)

    def euclid_recursive(self, first, second):
        if second == 0:
            return first
        return self.euclid_recursive(second, first % second)

    def lcm(self):
        return self.first * self.second / self.euclid()


class TestGCD(unittest.TestCase):
    def test_euclid(self):
        gcd = GCD(2336, 1314)
        self.assertEqual(gcd.euclid(), 146)
        self.assertEqual(gcd.lcm(), 21024)
