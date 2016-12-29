import unittest
"""
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15...
shows the first 11 ugly numbers. By convention, 1 is included.
Find the kth ugly number.
"""


def ugly_number(k):

    ugly_numbers = [1]
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    i2 = 0
    i3 = 0
    i5 = 0

    for i in range(2, k+1):
        next_ugly_number = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
        ugly_numbers.append(next_ugly_number)
        if next_ugly_number == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly_numbers[i2]*2
        if next_ugly_number == next_multiple_of_3:
            i3 += 1
            next_multiple_of_3 = ugly_numbers[i3]*3
        if next_ugly_number == next_multiple_of_5:
            i5 += 1
            next_multiple_of_5 = ugly_numbers[i5]*5
    return ugly_numbers[k-1]


class TestUglyNumbers(unittest.TestCase):

    def test_ugly_numbers(self):
        k = 150
        self.assertEqual(ugly_number(k), 5832)
