"""
Given an array arr of size n, three elements arr[i], arr[j] and arr[k] form an inversion of size 3
if arr[i] > arr[j] > arr[k] and i < j < k. Find the total number of inversions of size 3.
Input: 8 4 2 1
Output: 4
"""

"""
Approach 1:
1. For each element, check if this element can be middle element of an inversion.
2. To do this, we can count how many elements to its right are smaller than it.
3. Also, how many elements to its left are greater than it.
4. Number of inversions with this element as middle is smaller * greater.
5. Time complexity is O(n^2).
"""


def count_inversions_simple(list_of_numbers):

    num_inversions = 0
    end = len(list_of_numbers)
    for i in range(end):
        smaller_to_right = 0
        for j in range(i+1, end):
            if list_of_numbers[i] > list_of_numbers[j]:
                smaller_to_right += 1
        greater_to_left = 0
        for j in range(i):
            if list_of_numbers[i] < list_of_numbers[j]:
                greater_to_left += 1
        num_inversions += smaller_to_right * greater_to_left

    return num_inversions
