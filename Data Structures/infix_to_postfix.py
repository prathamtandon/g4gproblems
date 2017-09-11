import unittest
"""
Infix expression is of the form a op b, where a and b are operands and op is operator. Postfix expression is
of the form a b op. Evaluation of infix expression requires multiple scans of the input, therefore it is not
efficient. Postfix expression can be evaluated in single pass. Write a program to convert infix expression to
postfix expression.
Input: a+b*c+d
Output: abc*+d+
"""

"""
Approach:
1. We will use a stack to implement the algorithm.
2. Scan from left to right. If element is operand, then we print it.
3. If element is operator, then:
    (a) Push the operator on stack either if stack is empty or item currently on stack has lower precedence
    (b) Keep popping from stack and appending to output as long as item currently on stack has greater or equal
        precedence
4. If element is '(', we push it on the stack.
5. If element is ')', then we keep popping and appending to output till we encounter corresponding '('.
6. After scanning, append remaining items from stack to output, if any.
"""


def infix_to_postfix(infix):
    stack = []
    postfix = []

    for i in range(len(infix)):
        if is_operand(infix[i]):
            postfix.append(infix[i])
        elif is_operator(infix[i]):
            handle_operator(infix[i], stack, postfix)
        elif infix[i] == '(':
            stack.insert(0, infix[i])
        elif infix[i] == ')':
            handle_right_paren(stack, postfix)

    while len(stack) > 0:
        postfix.append(stack.pop(0))
    return ''.join(postfix)


def is_operand(ch):
    return not is_operator(ch) and ch != '(' and ch != ')'


def is_operator(ch):
    return ch == '+' or ch == '-' or ch == '*' or ch == '/' or ch == '^'


def handle_operator(ch, stack, postfix):
    precedence_ch = precedence(ch)
    while len(stack) > 0 and precedence(stack[0]) >= precedence_ch:
        postfix.append(stack.pop(0))
    stack.insert(0, ch)


def precedence(ch):
    if ch == '+' or ch == '-':
        return 1
    elif ch == '*' or ch == '/':
        return 2
    elif ch == '^':
        return 3
    else:
        return -1


def handle_right_paren(stack, postfix):
    while len(stack) > 0 and stack[0] != '(':
        postfix.append(stack.pop(0))
    if len(stack) > 0:
        stack.pop(0)
    # else:
    #     print 'Unbalanced parenthesis!'


class TestInfixToPostfix(unittest.TestCase):

    def test_infix_to_postfix(self):
        infix = 'a+b*(c^d-e)^(f+g*h)-i'
        self.assertEqual(infix_to_postfix(infix), 'abcd^e-fgh*+^*+i-')
