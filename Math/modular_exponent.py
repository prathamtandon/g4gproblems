import unittest
"""
Given three numbers x, y and p, compute (x^y)%p.
Input: x = 2, y = 3, p = 5
Output: 3
Input: x = 2, y = 5, p = 13
Output: 6
"""

# Iterative function to compute (x^y)%p in log(y)


def power(x, y, p):
    result = 1
    x = x % p  # update x if its >= p
    while y > 0:
        # If y is odd, multiply result by x
        if y & 1 > 0:
            result = (result * x) % p
        # y must be even now
        y >>= 1  # y = y/2
        x = (x * x) % p   # change x to x^2
    return result


class TestModularExponent(unittest.TestCase):

    def test_modular_exponent(self):
        self.assertEqual(power(2, 5, 13), 6)

