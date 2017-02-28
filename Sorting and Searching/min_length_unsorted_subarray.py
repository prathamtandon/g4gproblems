import unittest
"""
Given an unsorted array arr[0...n-1] of size n, find the minimum length subarray arr[s...e] such that
sorting this subarray makes the whole array sorted.
Input: 10 12 20 30 25 40 32 31 35 50 60
Output: subarray starting index 3 and ending index 8.
"""

"""
Approach:
1. Scan from left to right and find the first element which is out of place (ie element is smaller than its
   predecessor). Note its index.
2. Scan from right to left and find the first element which is out of place (ie element is larger than its
   predecessor). Note its index.
3. This gives us a candidate subarray. Now, we need to find if this is minimum length or not.
4. Find minimum and maximum values in candidate subarray.
5. Scan from start of subarray towards left, if there is an element which is larger than minimum, then
   set start of subarray at this element.
6. Similarly, scan from end of subarray towards right, if there is an element which is smaller than maximum,
   then set end of subarray at this element.
"""


def min_length_unsorted_subarray(arr):

    n = len(arr)
    start = 0
    end = n-1

    while start < n-1 and arr[start] <= arr[start+1]:
        start += 1

    while end > 0 and arr[end] >= arr[end-1]:
        end -= 1

    if start == n-1 and end == 0:
        return None

    min_ele = min(arr[start:end+1])
    max_ele = max(arr[start:end+1])

    i = 0
    while i < start:
        if arr[i] > min_ele:
            break
        i += 1

    if i != start:
        start = i

    j = n-1
    while j > end:
        if arr[j] < max_ele:
            break
        j -= 1

    if j != end:
        end = j

    return start, end


class TestMinLength(unittest.TestCase):

    def test_min_length(self):
        arr = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
        start, end = min_length_unsorted_subarray(arr)
        self.assertEqual(start, 3)
        self.assertEqual(end, 8)
        arr = [0, 1, 15, 25, 6, 7, 30, 40, 50]
        start, end = min_length_unsorted_subarray(arr)
        self.assertEqual(start, 2)
        self.assertEqual(end, 5)
