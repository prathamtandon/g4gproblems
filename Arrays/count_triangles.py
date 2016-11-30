import unittest
"""
Given an unsorted array of positive integers, find the number of triangles that
can be formed with three different array elements as three sides of triangles. NOTE:
If a triangle has three sides, say, a, b and c, all of the following must hold:
1. a + b > c
2. b + c > a
3. a + c > b
Input: 4 6 3 7
Output: 3 [(4,6,3),(4,6,7),(3,6,7)] (4,3,7) is not a valid triangle
Input: 10 100 101 21 22 300 200
Output: 6
"""

"""
Approach:
1. Sort the list of positive integers
2. Fix index i to leftmost element of list.
3. Fix index j to next element in list.
4. Move index k to rightmost element in the list such that list[i]+list[j]>list[k]
5. Increase the triangles count by k-j.
6. Time Complexity is O(N^2). It looks more like O(N^3) however, the combined inner loop with index j and
    inner loop with index k, run for at most O(N) for a single outermost loop iteration. So, complexity
    is O(N^2).
"""


def count_possible_triangles(list_of_numbers):

    list_of_numbers.sort()
    triangles_count = 0
    length = len(list_of_numbers)

    for i in range(length-2):
        for j in range(i+1, length-1):
            sum_of_first_two = list_of_numbers[i] + list_of_numbers[j]
            k = j+1
            while k < length and sum_of_first_two > list_of_numbers[k]:
                k += 1
            if k > j+1:
                triangles_count += k-j-1

    return triangles_count


class TestPossibleTriangles(unittest.TestCase):

    def test_possible_triangles(self):

        self.assertEqual(count_possible_triangles([4, 6, 3, 7]), 3)
        self.assertEqual(count_possible_triangles([10, 100, 101, 21, 22, 300, 200]), 6)
