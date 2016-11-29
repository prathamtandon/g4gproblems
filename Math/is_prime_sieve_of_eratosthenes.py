import unittest
"""
This method is used to generate all primes upto given value n.
First maintain a list of numbers from 2 through n. Start with first number, say p.
If p is not prime, mark p, 2p, 3p and so on as not prime. Then try with next p.
Finally, all numbers which have not been marked are the ones which are primes.
"""


def is_prime_sieve_of_eratosthenes(n):

    marked = [True] * (n+1)
    i = 2

    while i*i <= n:
        if marked[i] is False:
            i += 1
            continue
        for multiple in range(2*i, n+1, i):
            marked[multiple] = False
        i += 1

    return [i for i in range(2, n+1) if marked[i] is True]


class TestSieveOfEratosthenes(unittest.TestCase):

    def test_sieve_of_eratosthenes(self):
        self.assertEqual(is_prime_sieve_of_eratosthenes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
