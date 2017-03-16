import unittest
"""
Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.
Input: 1 2 3 1 4 5 2 3 6, k = 3
Output: 3 3 4 5 5 5 6
"""

"""
Approach:
1. This can be done in O(n) time complexity using a Double ended queue (Dequeue).
2. The idea is to only add useful elements into Dequeue. An element is useful if its present in
   current window, and its greater than all elements to its left.
3. New elements are always added at rear end of queue. Maximum element is always present at front of queue.
4. As, we move window forward, we remove those elements from front of queue which are no longer in current
   window.
Space complexity: O(k)
"""


def max_sliding_window(arr, k):
    dq = []
    n = len(arr)
    result = []

    # Process the first k items in arr
    for i in range(k):
        # Remove elements from dequeue smaller than current element
        while len(dq) > 0 and arr[i] >= arr[dq[len(dq)-1]]:
            dq.pop(len(dq)-1)
        # Add current item at back of dequeue
        dq.append(i)

    # Process the remaining items
    for i in range(k, n):
        # Add element at front of dequeue to result
        result.append(arr[dq[0]])
        # Remove elements from front no longer in current window
        while len(dq) > 0 and dq[0] <= i - k:
            dq.pop(0)
        # Remove elements from dequeue smaller than current element
        while len(dq) > 0 and arr[i] >= arr[dq[len(dq)-1]]:
            dq.pop(len(dq)-1)
        # Add current item at back of dequeue
        dq.append(i)

    result.append(arr[dq[0]])

    return result


class TestSliding(unittest.TestCase):

    def test_sliding(self):
        arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
        self.assertEqual(max_sliding_window(arr, 3), [3, 3, 4, 5, 5, 5, 6])
        arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
        self.assertEqual(max_sliding_window(arr, 4), [10, 10, 10, 15, 15, 90, 90])
