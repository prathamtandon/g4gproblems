import unittest
"""
Given two sorted arrays, find their union and intersection.
Input: 1 3 4 5 7, 2 3 5 6
Ouput: Union => 1 2 3 4 5 6 7 Intersection => 3 5
"""


def sorted_arrays_union(first_sorted, second_sorted):
    first_index = 0
    second_index = 0
    union = []

    while first_index < len(first_sorted) and second_index < len(second_sorted):
        if first_sorted[first_index] < second_sorted[second_index]:
            union.append(first_sorted[first_index])
            first_index += 1
        elif second_sorted[second_index] < first_sorted[first_index]:
            union.append(second_sorted[second_index])
            second_index += 1
        else:
            union.append(first_sorted[first_index])
            first_index += 1
            second_index += 1

    while first_index < len(first_sorted):
        union.append(first_sorted[first_index])
        first_index += 1

    while second_index < len(second_sorted):
        union.append(second_sorted[second_index])
        second_index += 1

    return union


def sorted_array_intersection(first_sorted, second_sorted):
    first_index = 0
    second_index = 0
    intersection = []

    while first_index < len(first_sorted) and second_index < len(second_sorted):
        if first_sorted[first_index] < second_sorted[second_index]:
            first_index += 1
        elif second_sorted[second_index] < first_sorted[first_index]:
            second_index += 1
        else:
            intersection.append(first_sorted[first_index])
            first_index += 1
            second_index += 1

    return intersection


class TestUnionAndIntersection(unittest.TestCase):

    def test_union_and_intersection(self):
        first_sorted = [1, 3, 4, 5, 7]
        second_sorted = [2, 3, 5, 6]

        self.assertEqual(sorted_arrays_union(first_sorted, second_sorted), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(sorted_array_intersection(first_sorted, second_sorted), [3, 5])


if __name__ == '__main__':
    unittest.main()
