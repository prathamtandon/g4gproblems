import unittest
"""
Given an array of integers, print the missing elements that lie in range 0-99.
Note that input array may not be sorted, and may contain numbers outside the range 0-99.
Input: 88 105 3 2 200 0 10
Output: 1, 4-9, 11-87, 89-99
"""


def find_missing_elements_between_0_and_99(list_of_numbers):

    found = [False] * 100
    end = len(list_of_numbers)

    for i in range(end):
        number = list_of_numbers[i]
        if number < 0 or number > 99:
            continue
        found[number] = True

    result = []
    end = len(found)
    lower = -1
    higher = -1

    for i in range(end):
        if found[i] is True:
            if lower > 0 and higher > 0:
                result.append((lower, higher))
                lower = -1
                higher = -1
            elif lower > 0:
                result.append(lower)
                lower = -1
        else:
            if lower == -1:
                lower = i
            else:
                higher = i

    if lower > 0 and higher > 0:
        result.append((lower, higher))
    elif lower > 0:
        result.append(lower)
    return result


class TestMissingElements(unittest.TestCase):

    def test_missing_elements(self):
        list_of_numbers = [88, 105, 3, 2, 200, 0, 10]
        result = find_missing_elements_between_0_and_99(list_of_numbers)
        self.assertEqual(len(result), 4)
        self.assertIn(1, result)
        self.assertIn((4, 9), result)
        self.assertIn((11, 87), result)
        self.assertIn((89, 99), result)

