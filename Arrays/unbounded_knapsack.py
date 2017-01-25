import unittest


def unbounded_knapsack(W, weights, values):
    # table[i] denotes the maximum value obtained with left capacity equal to i
    # table[W] stores the final result
    table = [-float('inf')] * (W+1)
    table[0] = 0

    for i in range(1, W+1):
        for j in range(len(weights)):
            if i - weights[j] >= 0:
                table[i] = max(table[i], table[i-weights[j]] + values[j])

    return table[W]


class TestUnboundedKnapsack(unittest.TestCase):

    def test_unbounded_knapsack(self):
        self.assertEqual(unbounded_knapsack(100, [1, 50], [1, 30]), 100)
        self.assertEqual(unbounded_knapsack(8, [1, 3, 4, 5], [10, 40, 50, 70]), 110)
