import unittest
"""
Given an array of positive and negative numbers, arrange them in alternate fashion
such that every positive number is followed by a negative number and vice-versa. You should
maintain the order of appearance.
Input: 1 2 3 -4 -1 4
Output: -4 1 -1 2 3 4
"""

"""
Approach 1:
1. Scan the array from left to right. Stop when there are two adjacent numbers with opposite sign.
2. Keep swapping until adjacent numbers have different signs.
"""

"""
Approach 2:
1. Scan the array from left to right.
2. Find the first number which is out of place - a negative number at odd index or a positive number at even index.
3. After finding out of place number, find the first element to its right with opposite sign.
4. Right rotate the array between these two numbers by 1 position.
"""


def same_sign(x, y):
    return (x > 0 and y > 0) or (x < 0 and y < 0)


def rearrange_no_rotation(arr):

    end = len(arr)

    for i in range(end-1):
        if same_sign(arr[i], arr[i+1]):
            continue
        j = i+1
        k = i-1

        while j >= 0 and k >= 0 and not same_sign(arr[j], arr[k]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
            k -= 1


def is_out_of_place(number, index):
    return (number < 0 and index % 2 != 0) or (number > 0 and index % 2 == 0)


def right_rotate(list_of_numbers, start, end, how_many):

    while how_many > 0:
        temp = list_of_numbers[end]
        for i in range(end, start, -1):
            list_of_numbers[i] = list_of_numbers[i-1]
        list_of_numbers[start] = temp
        how_many -= 1


def rearrange_with_rotation(list_of_numbers):

    end = len(list_of_numbers)
    out_of_place = -1

    for i in range(end):

        # check if current number is out of place
        if out_of_place == -1 and is_out_of_place(list_of_numbers[i], i):
            out_of_place = i

        elif out_of_place >= 0 and not same_sign(list_of_numbers[i], list_of_numbers[out_of_place]):
            right_rotate(list_of_numbers, out_of_place, i, 1)
            # now out_of_place and the number next to it are no longer out of place (Think about it!)
            # so, next potential out_of_place can be two steps ahead from current
            if i - out_of_place > 2:
                out_of_place += 2
            else:
                out_of_place = -1


class TestRearrange(unittest.TestCase):

    def test_rearrange_no_rotation(self):
        arr = [1, 2, 3, -4, -1, 4]
        rearrange_no_rotation(arr)
        self.assertEqual(arr, [1, -4, 2, -1, 3, 4])
        arr = [-5, -2, 5, 2, 4, 7, 1, 8, -10, -8]
        rearrange_no_rotation(arr)
        self.assertEqual(arr, [-5, 5, -2, 2, -10, 4, -8, 7, 1, 8])

    def test_rearrange_rotation(self):
        arr = [1, 2, 3, -4, -1, 4]
        rearrange_with_rotation(arr)
        self.assertEqual(arr, [-4, 1, -1, 2, 3, 4])
        arr = [-5, -2, 5, 2, 4, 7, 1, 8, -10, -8]
        rearrange_with_rotation(arr)
        self.assertEqual(arr, [-5, 5, -2, 2, -10, 4, -8, 7, 1, 8])






