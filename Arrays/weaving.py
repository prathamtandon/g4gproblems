import unittest
"""
Given two lists, generate all possible weaving of the lists such that the relative order is
maintained.
Input: [1, 2] and [3, 4]
Output:
[1, 2, 3, 4]
[3, 4, 1, 2]
[1, 3, 2, 4]
[3, 1, 2, 4]
[1, 3, 4, 2]
[3, 1, 4, 2]
"""


def weaving(list1, list2):
    if len(list1) == 0:
        return [list2]
    if len(list2) == 0:
        return [list1]
    result = []
    for l in weaving(list1[1:], list2):
        result.append([list1[0]] + l)
    for l in weaving(list1, list2[1:]):
        result.append([list2[0]] + l)
    return result


class TestWeaving(unittest.TestCase):

    def test_weaving(self):
        list1 = [1, 2]
        list2 = [3]
        self.assertEqual(weaving(list1, list2), [[1, 2, 3], [1, 3, 2], [3, 1, 2]])
