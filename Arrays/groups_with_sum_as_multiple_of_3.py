import unittest
"""
Given an unsorted array of positive integers, find count of all possible groups of either 2
or 3 integers, whose sum is a multiple of 3.
Input: 3 2 6 7 9
Output: 8
"""

"""
Approach:
1. Find the remainders of dividing each integer by 3.
2. Integers can form a group, if the sum of their respective remainders is a multiple of 3.
3. Create a hash table of different possible remainders of dividing integers by 3 (namely, 0, 1 and 2), whose
value is the count of integers from the list whose with that remainder.
NOTE: C(n,r) is the combinatorics function.
4. For groups of 2, we have two possibilities:
(a) C(hash_table[0],2)
(b) hash_table[1]*hash_table[2]
5. For groups of 3, we have four possibilities:
(a) C(hash_table[0],3)
(b) C(hash_table[1],3)
(c) C(hash_table[2],3)
(d) hash_table[0]*hash_table[1]*hash_table[3]
6. The answer is sum of counts from above steps.
"""


def n_c_2(n):
    return n * (n - 1) / 2


def n_c_3(n):
    return n * (n - 1) * (n - 2) / 6


def calculate_remainder_table(list_of_numbers, divisor):
    remainder_table = {}
    for number in list_of_numbers:
        remainder = number % divisor
        count = remainder_table.get(remainder, 0)
        count += 1
        remainder_table[remainder] = count
    return remainder_table


def calculate_2_groups_count(remainder_table):
    count = 0
    count += n_c_2(remainder_table[0])
    count += remainder_table[1] * remainder_table[2]
    return count


def calculate_3_groups_count(remainder_table):
    count = 0
    count += n_c_3(remainder_table[0])
    count += n_c_3(remainder_table[1])
    count += n_c_3(remainder_table[2])
    count += remainder_table[0] * remainder_table[1] * remainder_table[2]
    return count


def count_groups_with_sum_as_multiple_of_3(list_of_numbers):

    group_count = 0
    remainder_table = calculate_remainder_table(list_of_numbers, 3)
    group_count += calculate_2_groups_count(remainder_table)
    group_count += calculate_3_groups_count(remainder_table)

    return group_count


class TestGroupSum(unittest.TestCase):

    def test_group_sum(self):
        list_of_numbers = [3, 2, 7, 6, 9]
        self.assertEqual(count_groups_with_sum_as_multiple_of_3(list_of_numbers), 8)

