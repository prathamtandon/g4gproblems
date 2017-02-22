import unittest
"""
Print all jumping numbers smaller than or equal to a given value.
A number is called a jumping number if all adjacent digits in it differ by 1.
All single digit numbers are considered jumping numbers. For example, 7, 8987 and 4343456
are jumping numbers but 796 and 89098 are not.
"""

"""
Approach: Idea is to BFS and DFS starting at node 0. The neighbour of a node
will be last_digit in node + 1 and last_digit in node - 1 (except when last digit is 0 or 9).
"""


def bfs(start, x, numbers):
    queue = [start]
    while len(queue) > 0:
        cur = queue.pop(0)
        if cur > x:
            continue
        numbers.append(cur)
        last_digit = cur % 10
        if last_digit == 0:
            queue.append(cur * 10 + (last_digit + 1))
        elif last_digit == 9:
            queue.append(cur * 10 + (last_digit - 1))
        else:
            queue.append(cur * 10 + (last_digit + 1))
            queue.append(cur * 10 + (last_digit - 1))


def jumping_numbers(x):
    numbers = [0]
    for i in range(1,10):
        bfs(i, x, numbers)
    return numbers


class TestJumpingNumbers(unittest.TestCase):

    def test_jumping(self):
        self.assertItemsEqual(jumping_numbers(20), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12])
