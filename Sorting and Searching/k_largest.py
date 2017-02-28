import unittest
from random import randint
"""
Write a program for printing the k largest elements in an array. Elements in array can be in any order.
Input: 1 23 12 9 30 2 50
Output: 50, 30 and 23
"""

"""
Approach:
1. We can use Order-statistics to find the kth largest element in array. Then return all elements to its left
   inclusive.
2. We can also create a min-heap using the first k elements. Then for each remaining element, compare with
   root of min-heap. If greater than root, then swap and heapify. At the end, min-heap will contain the k
   largest elements.
3. Below we have implementation of Order-statistics with randomization.

NOTE: Same can also be achieved using a BST in which every node stores the number of nodes in its left subtree.
If k == left_count+1:
    return current_node
elif k < left_count:
    current_node = current_node.left
else:
    k = k - (left_count+1)
    current_node = current_node.right
"""


def k_largest_helper(arr, low, high, k):
    if 0 < k <= high - low + 1:
        pivot = random_partitioner(arr, low, high)
        if k-1 == pivot-low:
            return pivot
        if k-1 < pivot-low:
            return k_largest_helper(arr, low, pivot-1, k)
        return k_largest_helper(arr, pivot+1, high, k-pivot+low-1)


def random_partitioner(arr, low, high):
    n = high-low+1
    pivot = randint(low, high) % n
    arr[low+pivot], arr[high] = arr[high], arr[low+pivot]
    return partition(arr, low, high)


def partition(arr, low, high):

    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def k_largest(arr, k):
    n = len(arr)
    # k largest is n-k+1 smallest
    return k_largest_helper(arr, 0, n-1, n-k+1)


class TestKLargest(unittest.TestCase):

    def test_k_largest(self):
        arr = [1, 23, 12, 9, 30, 2, 50]
        result = k_largest(arr, 3)
        self.assertItemsEqual([50, 23, 30], arr[result:])
