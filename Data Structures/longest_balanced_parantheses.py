import unittest
"""
Given a string consisting of opening and closing parenthesis, find length of longest valid
parenthesis substring.
Input: ((()
Output: 2
Input: )()())
Output: 4
"""

"""
Approach:
1. Maintain a stack of indexes.
2. Scan the string from left to right.
3. If current character is '(' push it on top of stack.
4. If current character is ')', then pop from the stack. Now two cases:
    (a) If popped character is '(', then calculate current balanced substring length as current index - top of stack.
    (b) Otherwise, push ')' on top of stack.
"""


def longest_balanced(string):

    stack = [-1]
    max_len = -float('inf')

    for i in range(len(string)):
        if string[i] == '(':
            stack.insert(0, i)
        elif len(stack) > 0:
            top = stack.pop(0)
            if string[top] == '(':
                max_len = max(max_len, i - stack[0])
            else:
                stack.insert(0, i)

    return max_len


class TestLongestBalanced(unittest.TestCase):

    def test_longest_balanced(self):
        self.assertEqual(longest_balanced('()'), 2)
        self.assertEqual(longest_balanced('(((()'), 2)
        self.assertEqual(longest_balanced(')()()'), 4)
        self.assertEqual(longest_balanced('((()))(()'), 6)
