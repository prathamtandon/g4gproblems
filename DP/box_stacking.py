import unittest
"""
Given a set of n types of rectangular 3-D boxes, where the i'th box has height h[i], width w[i]
and depth d[i]. You have to create a stack of boxes which is as tall as possible. You can only
stack a box on top of another box if the dimensions of the 2-D base of lower box are each strictly
larger than those of the 2-D base of the higher box.
For given solution, assume box is an array of the form [height, width, depth].
"""

"""
Approach:
The idea is to have three instances of each box from the original set of boxes. For example, if there
is a box with dimensions: 1 x 2 x 3, then we have three instances of it:
(a) height = 1 and base = (2 x 3)
(b) height = 2 and base = (1 x 3)
(c) height = 3 and base = (1 x 2)
For simplicity we will assume that width <= depth.
Now, we sort the boxes in increasing order of their base ie (w1, d1) will come before (w2, d2) iff w1 < w2 and
d1 < d2. Given this sequence, for each box, we find the longest increasing sub-sequence ending in that box.
Length of a sub-sequence = sum of heights of boxes which are part of that sub-sequence.
"""


def box_comparator(box1, box2):
    return box1[2] * box1[1] - box2[2] * box2[1]


def box_stacking(boxes):
    n = len(boxes)
    rotated = []
    for i in range(n):
        rotated.append(boxes[i])
        rotated.append([boxes[i][1], min(boxes[i][0], boxes[i][2]), max(boxes[i][0], boxes[i][2])])
        rotated.append([boxes[i][2], min(boxes[i][0], boxes[i][1]), max(boxes[i][0], boxes[i][1])])

    rotated = sorted(rotated, cmp=box_comparator)
    n = len(rotated)
    # table[i] denotes the tallest stack formed with rotated[i] as the base.
    table = [0] * n

    for i in range(n):
        table[i] = rotated[i][0]

    for i in range(1, n):
        for j in range(i):
            if rotated[i][1] > rotated[j][1] and rotated[i][2] > rotated[j][2] and table[i] < table[j] + rotated[i][0]:
                table[i] = table[j] + rotated[i][0]

    return max(table)


class TestBoxStacking(unittest.TestCase):

    def test_box_stacking(self):
        boxes = [[4, 6, 7], [1, 2, 3], [4, 5, 6], [10, 12, 32]]
        self.assertEqual(box_stacking(boxes), 60)
