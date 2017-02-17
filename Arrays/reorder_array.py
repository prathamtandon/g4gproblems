"""
Given two integer arrays of same size, arr[] and index[], reorder elements in arr[] according to given index array.
Input:
arr: 50 40 70 60 90
index: 3 0 4 1 2
Output:
arr: 60 50 90 40 70
index: 0 1 2 3 4
"""

"""
Approach:
1. Do the following for every element arr[i]
2. While index[i] != i, store array and index values for the target position where arr[i] has to be placed.
    The correct position for arr[i] is index[i].
3. Place arr[i] at its correct position. Also update index value of correct position.
4. Copy old values of correct position to arr[i] and index[i] as the while loop continues for i.
"""


def reorder(list_of_numbers, indices):
    for i in range(len(list_of_numbers)):
        while indices[i] != i:
            old_target_index = indices[indices[i]]
            old_target_element = list_of_numbers[indices[i]]

            list_of_numbers[indices[i]] = list_of_numbers[i]
            indices[indices[i]] = indices[i]

            indices[i] = old_target_index
            list_of_numbers[i] = old_target_element


def reorder_2(list_of_numbers, indices):
    for i in range(len(list_of_numbers)):
        j = i
        temp = list_of_numbers[i]
        while indices[j] != i:
            target_index = indices[j]
            list_of_numbers[j] = list_of_numbers[target_index]
            indices[j] = j
            j = target_index
        list_of_numbers[j] = temp
        indices[j] = j



