import unittest
"""
Given n daily price quotes for a stock, we need to calculate span of stock's price for
all n days.
The Span S[i] of the stock's price on a given day i is defined as the maximum number of
consecutive days just before day i, for which price of stock on that day is less than
or equal to price of stock on day i.
Input: prices = {100, 80, 60, 70, 60, 75, 85}
Output: spans = {1, 1, 1, 2, 1, 4, 6}
"""

"""
Approach:
1. When computing span for day i, say the price of stock on that day is prices[i].
2. We need to find the first day j to left of i such that prices[j] > prices[i].
3. Then span for day i will be j - i. If there is no such day j, then span for day i is i + 1.
4. We use a stack to store indices. When we are at day i, we keep removing indices from stack
   till we find an index j on stack for which prices[j] > prices[i].
5. We then push i on stack.
"""


def stock_span(prices):
    spans = [0] * len(prices)
    spans[0] = 1
    stack = [0]

    for i in range(1, len(prices)):
        while len(stack) > 0 and prices[stack[-1]] <= prices[i]:
            stack.pop()

        spans[i] = (i + 1) if len(stack) == 0 else i - stack[-1]
        stack.append(i)

    return spans


class TestStockSpan(unittest.TestCase):

    def test_stock_span(self):
        prices = [100, 80, 60, 70, 60, 75, 85]
        self.assertEqual(stock_span(prices), [1, 1, 1, 2, 1, 4, 6])
        prices = [10, 4, 5, 90, 120, 80]
        self.assertEqual(stock_span(prices), [1, 1, 2, 4, 5, 1])

