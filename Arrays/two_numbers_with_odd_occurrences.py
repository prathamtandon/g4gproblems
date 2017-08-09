import unittest
"""
Given a list of unsorted numbers, all numbers appear even number of times, except two, which
occur odd number of times. Find the two odd occurring numbers.
Input: 12 23 34 12 12 23 12 45
Output: 34 and 45
Input: 4 4 100 5000 4 4 100 100
Output: 100 5000
Input: 10 20
Output: 10 20
"""

"""
Approach:
1. Say x and y are the two odd occurring numbers.
2. Find the XOR of all numbers in the list. This will give x XOR y.
3. Now, for all bits in x XOR y, which are 1, x and y have different bits in corresponding positions.
4. For all bits in x XOR y which are 0, x and y have same bits in corresponding positions.
5. We first find the rightmost bit which is 1. (rightmost_set_bit = x & ~(x-1))
6. Then we divide the numbers in the list into two groups, 1 group will have all numbers where this bit is 1,
   second group will have all numbers where this bit is 0.
7. This means all occurrences of same number will go into the same group.
8. Also, x and y will go into different groups.
9. If we take XOR of all values in each group, even occurrences of numbers will result in 0, leaving x in one group
   and y in the second.
"""


def find_two_odd_occurring_in_list(list_of_numbers):

    xor_of_list = 0
    for number in list_of_numbers:
        xor_of_list ^= number

    mask = xor_of_list & ~(xor_of_list - 1)

    missing_1 = 0
    missing_2 = 0

    for number in list_of_numbers:
        if number & mask > 0:
            missing_1 ^= number
        else:
            missing_2 ^= number

    return missing_1, missing_2


class TestTwoOddOccurring(unittest.TestCase):

    def test_two_odd_occurring_in_list(self):
        list_of_numbers = [12, 23, 34, 12, 12, 23, 12, 45]
        result = find_two_odd_occurring_in_list(list_of_numbers)
        self.assertIn(34, result)
        self.assertIn(45, result)

