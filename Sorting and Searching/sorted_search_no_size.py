"""
You are given an array-like data structure Listy which lacks a size method.
It does, however, have an elementAt(i) method that returns the element at index i in
O(1) time. If i is beyond the bounds of the data structure, it returns -1. Given a Listy
which contains sorted, positive integers, find the index at which an element x occurs.
If x occurs multiple times, you may return any index.
"""

"""
Approach:
1. The idea is to find the true end of Listy.
2. We can start at low, then increase index as powers of 2.
3. In this way, we can find the true end in O(log(n)) time. In worst case, we will overshoot the true end
   by a factor of 2.
4. Then, we run a binary search. If arr[mid] == -1, we set high = mid-1
"""


def search(list, key):
    index = 1
    while list.elementAt(index) != -1 and list.elementAt(index) < key:
        index *= 2
    return binary_search(list, key, index / 2, index)


def binary_search(list, low, high, key):
    if low > high:
        return -1
    mid = (low + high) >> 1
    if list.elementAt(mid) == -1 or list.elementAt(mid) > key:
        return binary_search(list, low, mid - 1, key)
    elif list.elementAt(mid) < key:
        return binary_search(list, mid + 1, high, key)
    return mid

