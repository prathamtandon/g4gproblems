"""
Returns true if given number is prime.
Introductory (school) method:
Test if n is prime => check for all values from 2 through sqrt(n) to see if the value divides n.
If no value divides n, then return True.
With the exclusion of 2 and 3, all primes are of the form 6k+1 or 6k-1. So, a better way to test is to
try all numbers of the form 6k+1 and 6k-1 instead of all numbers till sqrt(n).
"""


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i+2) == 0:
            return False
        i += 6

    return True
