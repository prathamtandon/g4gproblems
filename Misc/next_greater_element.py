import unittest
"""
Given an array, print next greater element. The NGE for an element x is the first greater
element on the right side of x in the array. Elements for which no greater element exist,
print -1.
Input: {4, 5, 2, 25}
Output: {5, 25, 25, -1}
"""


def next_greater(arr):
    nge = [-1] * len(arr)
    stack = [arr[-1]]

    for i in range(len(arr) - 2, -1, -1):
        while len(stack) > 0 and stack[-1] <= arr[i]:
            stack.pop()

        if len(stack) > 0:
            nge[i] = stack[-1]

        stack.append(arr[i])

    return nge


class TestNGE(unittest.TestCase):

    def test_nge(self):
        arr = [4, 5, 2, 25]
        self.assertEqual(next_greater(arr), [5, 25, 25, -1])
        arr = [13, 7, 6, 12]
        self.assertEqual(next_greater(arr), [-1, 12, 12, -1])
        arr = [11, 13, 21, 3]
        self.assertEqual(next_greater(arr), [13, 21, -1, -1])
