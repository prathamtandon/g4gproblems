import unittest
"""
Find the largest rectangular area possible in a given histogram where the largest
rectangle can be made of a number of contiguous bars. Each bar has different vertical heights,
but same width = 1 unit.
Input: 6 2 5 4 5 1 6
Output: 12
|
|_           _
| |  _   _  | |
| | | |_| | | |
| | | | | | | |
| |_| | | | | |
| | | | | |_| |
|_|_|_|_|_|_|_|_
"""

"""
Approach:
1. The idea is to maintain a stack.
2. If height of current item is greater than height of item on stack, we push the item.
3. Otherwise, we keep popping items till stack top item has greater height than current item.
4. While popping items, we use the following formula to compute area of histogram:
    (a) If stack is empty, area = height_of_popped_item * current_index
    (b) Else, area = height_of_popped_item * (current_index - stack[top] + 1)
5. Update maximum area so far as needed.
Note: Stack will store index of items, not actual heights.
"""


def compute_area(height, right, left):
    return height * (right-left-1)


def max_area_histogram(heights):
    stack = []
    max_so_far = -1e7

    for i in range(len(heights)):
        # If this bar is taller than bar on top of stack, we push on stack.
        if len(stack) == 0 or heights[stack[0]] <= heights[i]:
            stack.insert(0, i)
        # Otherwise, calculate area of rectangle with stack top as the minimum height bar.
        # Then push the current bar on top of stack, once the current top is smaller or equal in height.
        else:
            while len(stack) > 0 and heights[stack[0]] > heights[i]:
                top = stack.pop(0)
                # First argument is height, second argument is right edge of rectangle and third argument is
                # left edge.
                area = compute_area(heights[top], i, stack[0] if len(stack) > 0 else 0)
                max_so_far = max(max_so_far, area)
            stack.insert(0, i)

    # Repeat for any remaining bars.
    while len(stack) > 0:
        top = stack.pop(0)
        area = compute_area(heights[top], len(heights), stack[0] if len(stack) > 0 else 0)
        max_so_far = max(max_so_far, area)

    return max_so_far


class TestHistogram(unittest.TestCase):

    def test_histogram(self):
        heights = [6, 2, 5, 4, 5, 1, 6]
        self.assertEqual(max_area_histogram(heights), 12)
