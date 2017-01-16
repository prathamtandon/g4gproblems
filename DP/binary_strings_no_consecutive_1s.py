import unittest
"""
Given positive integer N, find the number of binary strings with N digits
that have no consecutive 1s.
Input: N = 2
Output: 3 (00, 10, 01)
"""

"""
Approach:
1. Let a[i] denote number of binary strings of length i ending in 0 without consecutive 1s.
2. Let b[i] denote number of binary strings of length i ending in 1 without consecutive 1s.
3.  a[i] = a[i-1] + b[i-1]
    b[i] = a[i-1]

Note: binary_strings(N) = (N+2)nd Fibonacci number
"""


def binary_strings(N):

    a = [0] * (N+1)
    b = [0] * (N+1)

    a[1] = 1
    b[1] = 1

    for i in range(2, N+1):
        a[i] = a[i-1] + b[i-1]
        b[i] = a[i-1]

    return a[N] + b[N]


class TestBinaryStrings(unittest.TestCase):

    def test_binary_strings(self):
        self.assertEqual(binary_strings(2), 3)
        self.assertEqual(binary_strings(3), 5)
