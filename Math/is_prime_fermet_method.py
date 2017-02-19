import unittest
"""
Fermet Little Theorem:
If n is prime, then for all integers 'a' such that 2 <= a <= n-1, a**(n-1) % n = 1.
Idea is to chose a random 'a' from the above mentioned range, k times, and return True if
remainder is 1 for each time.
This is a probabilistic method: It returns true for all primes, it may return true for composites (non-primes).
Higher k => greater accuracy.
"""

from random import randint


# Computes (a ** n) % p in O(log(n)) time complexity.
# If n == 0: return 1
# If n % 2 == 0:
# return a^(n/2) * a^(n/2)
# else return a * a^(n/2) * a^(n/2)
def modular_exponent(a, n, p):
    result = 1
    a = a % p

    while n > 0:
        # If exponent is odd, multiply result with num
        if n % 2 != 0:
            result = (result * a) % p

        # Exponent must be even now
        n /= 2
        a = (a * a) % p

    return result


def is_prime_fermet(number, num_iterations):

    if number <= 1 or number == 4:
        return False
    if number <= 3:
        return True

    while num_iterations > 0:

        a = randint(2, number-2)
        if modular_exponent(a, number-1, number) != 1:
            return False
        num_iterations -= 1

    return True


class TestPrimality(unittest.TestCase):

    def test_is_prime_fermet(self):
        self.assertTrue(is_prime_fermet(11, 3))
        self.assertFalse(is_prime_fermet(15, 3))
