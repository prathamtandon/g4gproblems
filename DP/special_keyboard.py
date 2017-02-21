import unittest
"""
Imagine you have a special keyboard with the following keys:
Key 1: Prints 'A' on screen
Key 2: (Ctrl-A): Select screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending it
                after what has already been printed.
If you can only press the keyboard for N times (with the above four
keys), write a program to produce maximum number of As.
"""

"""
Approach:
Requires "SPECIAL INSIGHT"
1. The idea is that if number of keystrokes is <= 6, maximum number of A's that can be printed is equal to
    number of keystrokes itself.
2. However, if number of keystrokes > 6, then optimal solution can be obtained only by pressing a series of As,
   the pressing Ctrl-A, Ctrl-C followed by only Ctrl-Vs for the remainder of keystrokes.
3. Using following recursive substructure, we can find out after how many presses of As, we should start pressing
   Ctrl-A, Ctrl-C and Ctrl-Vs thereafter:
   maxA(N (>6)) = max(maxA(b-1) * (N - b) for b = N-3,N-2,...,1))
   That is, we try all positions from N-3 to 1 to insert the sequence of Ctrl-A, Ctrl-C and Ctrl-V.
"""


def special_keyboard(N):

    if N <= 6:
        return N
    # table[i] stores the maximum number of A's that can be printed using i keystrokes.
    # table[N] stores the final result.
    table = [0] * (N+1)

    for i in range(7):
        table[i] = i

    for i in range(7, N+1):
        for j in range(i-2, 0, -1):
            table[i] = max(table[i], table[j-1] * (i - j))

    return table[N]


class TestSpecialKeyboard(unittest.TestCase):

    def test_special(self):
        self.assertEqual(special_keyboard(3), 3)
        self.assertEqual(special_keyboard(7), 9)
        self.assertEqual(special_keyboard(11), 27)
        self.assertEqual(special_keyboard(20), 324)

