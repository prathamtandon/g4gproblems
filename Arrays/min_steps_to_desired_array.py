import unittest
"""
Given an array with n elements, value of all the elements is zero.
We can perform following operations on the array:
1. Incremental operations:Choose 1 element from the array and increment its value by 1.
2. Doubling operation: Double the values of all the elements of array.
The desired array target[] contains n elements. Compute and return smallest possible number
of operations needed to change the array from all zeros to desired array.
Input: 2 3
Output: 4 (increment both zeros by 1 (2 ops), double them (1 op), increment 2nd 2 by 1 (1 op).
"""


"""
Approach:
1. Approach in reverse direction: make target array to an array of all zeros.
2. Decrement all odd elements by 1, increment count of operations for each such decrement.
3. Divide all elements by 2. Repeat from step 2 until all elements are zero.
"""


def min_steps_to_desired_array(target):

    num_ops = 0
    while True:
        for i in range(len(target)):
            if target[i] % 2 != 0:
                target[i] -= 1
                num_ops += 1
        if target.count(0) == len(target):
            break
        target = [x / 2 for x in target]
        num_ops += 1
    return num_ops


class TestMinSteps(unittest.TestCase):

    def test_min_steps(self):
        target = [2, 3]
        self.assertEqual(min_steps_to_desired_array(target), 4)
        target = [2, 1]
        self.assertEqual(min_steps_to_desired_array(target), 3)
        target = [16, 16, 16]
        self.assertEqual(min_steps_to_desired_array(target), 7)
