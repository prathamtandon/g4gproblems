import unittest
"""
Given heights of n towers and a value k. We need to either increase or decrease height of every tower by k
(only once) where k > 0. The task is to minimize the difference between the heights of the
longest and the shortest tower after modifications, and output this difference.
Input  : arr[] = {1, 15, 10}, k = 6
Output : arr[] = {7, 9, 4}
         Maximum difference is 5.
Explanation : We change 1 to 6, 15 to
9 and 10 to 4. Maximum difference is 5
(between 4 and 9). We can't get a lower
difference.
"""


def minimize_differnce_between_max_and_min_heights(list_of_heights, k):

    list_of_heights = sorted(list_of_heights)
    end = len(list_of_heights)
    # initialize tallest and shortest towers in original list.
    min_height = list_of_heights[0]
    max_height = list_of_heights[end - 1]

    # If k is greater than max and min difference, then k cannot further decrease the difference.
    if k > max_height - min_height:
        return max_height - min_height

    # Add k to minimum and subtract k from maximum.
    list_of_heights[0] += k
    list_of_heights[end - 1] -= k

    # Initialize tallest and shortest in modified list.
    min_height = min(list_of_heights[0], list_of_heights[end - 1])
    max_height = max(list_of_heights[0], list_of_heights[end - 1])

    # Fix middle n-2 elements.
    for j in range(1, end-1):
        # If current element is greater than max of modified array, subtract k.
        if list_of_heights[j] > max_height:
            list_of_heights[j] -= k
        # If current element is less than min of modified array, add k.
        elif list_of_heights[j] < min_height:
            list_of_heights[j] += k
        else:
            # current element is between min and max of modified list.
            # If closer to max, subtract k , else add k.
            if list_of_heights[j] - min_height > max_height - list_of_heights[j]:
                list_of_heights[j] -= k
            else:
                list_of_heights[j] += k
        # Update min and max heights if needed.
        min_height = min(min_height, list_of_heights[j])
        max_height = max(max_height, list_of_heights[j])

    return max_height - min_height


class TestDiffernceOfHeights(unittest.TestCase):

    def test_difference_of_heights(self):
        list_of_heights = [1, 15, 10]
        self.assertEqual(minimize_differnce_between_max_and_min_heights(list_of_heights, 6), 5)
