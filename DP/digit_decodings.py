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
    table[1] = 1

    for i in range(2, n+1):
        if digits[i-1] > '0':
            table[i] = table[i-1]
        if digits[i-2] < '2' or digits[i-2] == '2' and digits[i-1] < '7':
            table[i] += table[i-2]

    return table[n]


class TestDigitDecodings(unittest.TestCase):

    def test_digit_decodings(self):
        digits = '121'
        self.assertEqual(digit_decodings(digits), 3)
        digits = '1234'
        self.assertEqual(digit_decodings(digits), 3)
