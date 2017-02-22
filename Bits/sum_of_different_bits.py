import unittest
"""
We define f(X,Y) as number of different corresponding bits in binary representation of X and Y.
For example f(2, 7) = 2, since binary representation of 2 and 7 are 010 and 111, respectively.
The first and third bit differ, so f(2, 7) = 2.
You are given an array of N integers A1, A2, ..., AN. Find sum of f(Ai,Aj) for all pairs i,j
such that 1<=i,j<=N. Return the answer modulo 10^9+7.
"""

"""
Approach:
Note that f(X,X) = 0. So, we don't really have to worry about f(Ai,Ai) as that would not affect the result.
1. Assume that all numbers in array only consist of 1's and 0's. Say 1 count is A and 0 count is B.
2. Then, sum of different corresponding bits in all pairs is 2*A*B (Note that (1,0) and (0,1) both will add to sum)
3. We can generalize this for all numbers by considering only the ith bits for i = 0,1,...,31.
Time complexity is O(32*N).
"""


def sum_of_different_bits(arr):

    result = 0
    MOD = (10**9) + 7
    for i in range(32):
        one_count = 0
        for num in arr:
            if (num & (1 << i)) > 0:
                one_count += 1
        zero_count = len(arr) - one_count
        result += (2 * one_count * zero_count) % MOD
        result %= MOD
    return result


class TestSumDifferentBits(unittest.TestCase):

    def test_sum_different_bits(self):
        arr = [1, 3, 5]
        self.assertEqual(sum_of_different_bits(arr), 8)

