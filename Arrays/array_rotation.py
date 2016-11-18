import unittest
"""
Given an array of n elements, rotate it by d elements.
Input: 1 2 3 4 5 6 7, d = 2
Output: 3 4 5 6 7 1 2
"""


"""
Approach:
1. Rotate the array by 1, d times.
2. Hold first element in temp.
3. Move following elements one position to left.
4. Replace last element with temp.
"""


def array_left_rotate(list_of_numbers, num_rotations):
    length = len(list_of_numbers)
    while num_rotations > 0:
        temp = list_of_numbers[0]
        for i in range(length - 1):
            list_of_numbers[i] = list_of_numbers[i + 1]
        list_of_numbers[length - 1] = temp
        num_rotations -= 1


class TestLeftRotation(unittest.TestCase):

    def test_array_left_rotate(self):
        list_of_numbers = [1, 2, 3, 4, 5, 6, 7]
        num_rotations = 2
        array_left_rotate(list_of_numbers, num_rotations)
        self.assertEqual(list_of_numbers, [3, 4, 5, 6, 7, 1, 2])


if __name__ == '__main__':
    unittest.main()
