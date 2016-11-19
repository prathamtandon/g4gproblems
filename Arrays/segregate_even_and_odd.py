import unittest
"""
Given an array, segregate odd and even numbers such that all even numbers come
before the odd numbers.
Input: 12 34 45 9 11 90 4
Output: 12 34 90 4 45 9 11
"""


def segregate_odd_and_even(list_of_numbers):
    length = len(list_of_numbers)
    even_index = 0
    odd_index = length - 1

    while even_index < odd_index:
        while list_of_numbers[even_index] % 2 == 0:
            even_index += 1
        while list_of_numbers[odd_index] % 2 != 0:
            odd_index -= 1
        list_of_numbers[even_index], list_of_numbers[odd_index] = \
            list_of_numbers[odd_index], list_of_numbers[even_index]
        even_index += 1
        odd_index -= 1


class TestSeparateOddAndEven(unittest.TestCase):

    def test_segregate_odd_and_even(self):
        list_of_numbers = [12, 34, 45, 9, 11, 90, 4]
        segregate_odd_and_even(list_of_numbers)
        self.assertEqual(list_of_numbers, [12, 34, 4, 90, 11, 9, 45])


if __name__ == '__main__':
    unittest.main()
