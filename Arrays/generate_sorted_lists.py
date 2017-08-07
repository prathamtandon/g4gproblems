"""
Given two sorted arrays A and B, generate all possible arrays such that first element is taken
from A then from B then from A and so on in increasing order till the arrays are exhausted. The generated
arrays should end in an element from B.
Input:
A: 10 15 25
B: 1 5 20 30
Output:
10 20
10 20 25 30
10 30
15 20
15 20 25 30
15 30
25 30
"""


def generate_sorted_from_first(A, B, i, j, result):
    print result
    last = B[j]
    k = find_ceil(A, i + 1, len(A) - 1, last)
    if k < len(A) and A[k] < last:
        return
    else:
        while k < len(A):
            generate_sorted_from_second(A, B, k, j, result + [A[k]])
            k += 1


def generate_sorted_from_second(A, B, i, j, result):
    if j == len(B) - 1:
        return
    else:
        last = A[i]
        k = find_ceil(B, j + 1, len(B) - 1, last)
        if k < len(B) and B[k] < last:
            return
        else:
            while k < len(B):
                generate_sorted_from_first(A, B, i, k, result + [B[k]])
                k += 1


def find_ceil(A, low, high, key):
    while low < high:
        mid = (low + high) / 2
        if A[mid] < key:
            low = mid + 1
        else:
            high = mid
    return low


if __name__ == '__main__':

    first_sorted = [10, 15, 25]
    second_sorted = [1, 5, 20, 30]

    for i in range(len(first_sorted)):
        generate_sorted_from_second(first_sorted, second_sorted, i, -1, [first_sorted[i]])



