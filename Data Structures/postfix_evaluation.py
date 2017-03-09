import unittest
"""
Expressions written in postfix expression are evaluated faster compared to infix notation
as postfix does not require parenthesis. Write program to evaluate postfix expression.
"""

"""
Approach:
1. Scan postfix expression from left to right.
2. If element is operand, we push it on the stack.
3. If element is operator, we pop the two most recent items from the stack, evaluate using them, and then push
   the result on stack.
4. Finally, the only value remaining in the stack is the output.
"""


def postfix_evaluate(postfix):
    stack = []

    for i in range(len(postfix)):
        if is_operand(postfix[i]):
            stack.insert(0, postfix[i])
        elif is_operator(postfix[i]):
            right_operand = stack.pop(0)
            left_operand = stack.pop(0)
            result = evaluate(left_operand, right_operand, postfix[i])
            stack.insert(0, result)

    return int(stack.pop(0))


def is_operand(ch):
    return not is_operator(ch) and ch != '(' and ch != ')'


def is_operator(ch):
    return ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '^'


def evaluate(lhs, rhs, op):
    lhs = int(lhs)
    rhs = int(rhs)
    if op == '+':
        return str(lhs + rhs)
    elif op == '-':
        return str(lhs - rhs)
    elif op == '*':
        return str(lhs * rhs)
    elif op == '/':
        return str(lhs / rhs)
    elif op == '^':
        return str(lhs ^ rhs)


class TestPostfixEvaluate(unittest.TestCase):

    def test_postfix_evaluate(self):
        self.assertEqual(postfix_evaluate('231*+9-'), -4)
