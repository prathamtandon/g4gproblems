import unittest
"""
Let 1 represent 'A', 2 represent 'B' etc. Given a digit sequence, count the number of possible decodings
given digit sequence.
Input: digits = '121'
Output: 3 ('ABA', 'AU', 'LA')
"""


def digit_decodings(digits):

    n = len(digits)
    # table[i] = number of decodings for digits[0:i]
    table = [0] * (n+1)
    table[0] = 1

    for i in range(1, n+1):
        for j in range(i-1, i-3, -1):
            if j >= 0 and 1 <= int(digits[j:i]) <= 26:
                table[i] += table[j]

    return table[n]


class TestDigitDecodings(unittest.TestCase):

    def test_digit_decodings(self):
        digits = '121'
        self.assertEqual(digit_decodings(digits), 3)
        digits = '1234'
        self.assertEqual(digit_decodings(digits), 3)
