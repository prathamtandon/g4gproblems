import unittest
"""
Given a list of intervals, return a new list in which overlapping intervals have been merged into single interval.
Input: [(1,3),(2,4),(5,7),(6,8)]
Output: [(1,4),(5,8)]
"""

"""
Approach:
1. Sort the intervals based on start times only in non-decreasing order.
2. In sorted list, compare adjacent elements.
3. For each adjacent pair, get the merged interval. Refer to merged_interval method to see how merging works.
4. Use the result from previous merge to compare against the current interval from the list.
5. If a disjoint interval pair is found, add current merged to list of merged.
"""


def interval_comparator(first, second):
    return first[0] - second[0]


def merged_interval(first, second):
    if first is None and second is not None:
        return second
    if first is not None and second is None:
        return first
    merged = None
    if first[0] < second[0] < first[1] < second[1]:
        merged = (first[0], second[1])
    elif first[0] < second[0] < second[1] < first[1]:
        merged = first
    elif second[0] < first[0] < first[1] < second[1]:
        merged = second
    elif second[0] < first[0] < second[1] < second[0]:
        merged = (second[0], first[1])
    return merged


def merge_overlapping(list_of_intervals):

    list_of_intervals = sorted(list_of_intervals, cmp=interval_comparator)
    merged_intervals = []
    current_interval = list_of_intervals[0]
    for i in range(1, len(list_of_intervals)):
        prev_interval = current_interval
        current_interval = merged_interval(current_interval, list_of_intervals[i])
        if current_interval is None:
            merged_intervals.append(prev_interval)
            current_interval = list_of_intervals[i]

    merged_intervals.append(current_interval)
    return merged_intervals


class TestMergedIntervals(unittest.TestCase):

    def test_merged_intervals(self):
        self.assertEqual(merge_overlapping([(1, 3), (5, 7), (2, 4), (6, 8)]), [(1, 4), (5, 8)])
        self.assertEqual(merge_overlapping([(6, 8), (1, 9), (2, 4), (4, 7)]), [(1, 9)])

