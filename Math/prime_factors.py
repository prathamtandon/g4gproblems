import unittest
"""
Given a number n, return its prime factors.
Input: 12
Output: 2 2 3
Input: 315
Output: 3 3 5 7
"""


"""
Approach:
1. While n is divisible by 2, print 2 and make n equals n divided by 2.
2. Now n will be odd. Start dividing by 3 till sqrt(n), while n is divisible, in steps of 2.
3. After this, if n will either be 1 or it will be a prime. If it's a prime greater than 2, add n as a prime
   factor.
"""


def prime_factors(number):

    factors = []

    while number % 2 == 0:
        number /= 2
        factors.append(2)

    i = 3
    while i*i <= number:
        while number % i == 0:
            number /= i
            factors.append(i)
        i += 2

    if number > 2:
        factors.append(number)

    return factors


class TestPrimeFactors(unittest.TestCase):

    def test_prime_factors(self):
        self.assertEqual(prime_factors(12), [2, 2, 3])
        self.assertEqual(prime_factors(315), [3, 3, 5, 7])
        self.assertEqual(prime_factors(1092), [2, 2, 3, 7, 13])



