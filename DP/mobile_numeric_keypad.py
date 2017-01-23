import unittest
"""
Given the mobile numeric keypad, you can only press buttons that are up, left, right or down
to the current button. You are not allowed to press bottom row corner buttons.
Given a number N, find out the number of possible numbers of given length.
Input: N = 1
Output: 10 (0,1,2...,9)
Input: N = 2
Output: 36 (00, 08, 11, 12, 14, 22, 21 and so on)
"""

"""
Approach:
Optimal Substructure:
mobile_keypad(N, start_char) = sum(mobile_keypad(N-1, next_char)) for next_char in valid_chars_from(start_char)
"""

valid_presses_from = {
    0: [0, 8],
    1: [1, 2, 4],
    2: [1, 2, 3, 5],
    3: [2, 3, 6],
    4: [1, 4, 5, 7],
    5: [2, 4, 5, 6, 8],
    6: [3, 5, 6, 9],
    7: [4, 7, 8],
    8: [0, 5, 7, 8, 9],
    9: [6, 8, 9]
}


def mobile_keypad(N):

    # table[i][j] is number of possible numbers starting at i and of length j
    # The final result is sum of values in last column.
    table = [[0] * (N+1) for _ in range(10)]

    for i in range(10):
        table[i][1] = 1

    for i in range(2, N+1):
        for j in range(10):
            for k in valid_presses_from[j]:
                table[j][i] += table[k][i-1]

    count = 0
    for i in range(10):
        count += table[i][N]

    return count


class TestMobileKeypad(unittest.TestCase):

    def test_mobile_keypad(self):
        self.assertEqual(mobile_keypad(1), 10)
        self.assertEqual(mobile_keypad(2), 36)
        self.assertEqual(mobile_keypad(3), 138)
        self.assertEqual(mobile_keypad(4), 532)
        self.assertEqual(mobile_keypad(5), 2062)

