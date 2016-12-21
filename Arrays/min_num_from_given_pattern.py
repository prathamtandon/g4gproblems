import unittest
"""
Given a pattern of only I's and D's where I stands for increasing and D stands for decreasing,
write an algorithm to print minimum number following that pattern. Digits are from 1-9 and cannot repeat.
Input: I
Output: 12
Input: D
Output: 21
Input: II
Output: 123
Input: DD
Output: 321
Input: DIDI
Output: 21435
Input: DDIDDIID
Output: 321654798
"""

"""
Approach: (Cannot comprehend without knowing the solution!)
1. Scan the first character.
2. If I, then append 1 and 2 to the output. Set minimum available digit to 3 and set position of most recent I to 1.
3. If D, then append 2 and 1 to the output. Set minimum available digit to 3 and set position of most recent I to 0.
4. Next, if we encounter I, then we append minimum available digit to output. We update both minimum available
    digit and most recent I index.
5. Otherwise, if we encounter D, then we copy the last appended digit into the output, and the increment
    all digits from most recent I to D by 1.
"""


def min_num_from_given_pattern(pattern):
    min_number = []
    if pattern[0] == 'I':
        min_number.append(1)
        min_number.append(2)
        next_available = 3
        most_recent_i = 1
    else:
        min_number.append(2)
        min_number.append(1)
        next_available = 3
        most_recent_i = 0

    for i in range(1, len(pattern)):
        if pattern[i] == 'I':
            min_number.append(next_available)
            most_recent_i = i+1
        else:
            end = len(min_number)
            min_number.append(min_number[end-1])
            for j in range(most_recent_i, i+1):
                min_number[j] += 1
        next_available += 1

    return int(''.join([str(x) for x in min_number]))


class TestMinNumber(unittest.TestCase):

    def test_min_number(self):
        pattern = 'II'
        self.assertEqual(min_num_from_given_pattern(pattern), 123)
        pattern = 'DD'
        self.assertEqual(min_num_from_given_pattern(pattern), 321)
        pattern = 'DDIDDIID'
        self.assertEqual(min_num_from_given_pattern(pattern), 321654798)
