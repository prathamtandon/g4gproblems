"""
Given an almost sorted array in ascending order where only two elements are swapped,
how to sort the array efficiently.
"""

"""
Approach:
1. Scan from left to right to find the first larger element on the left side ie x[i]>x[i+1]
2. Scan from n-1 down to i, and find the first j such that x[j]<=x[i+1]
3. Swap x[i] and x[j]
"""


def sort_almost_sorted(x):
    n = len(x)

    for i in range(n - 1):
        if x[i] > x[i + 1]:
            for j in range(n - 1, i, -1):
                if x[j] <= x[i + 1]:
                    x[i], x[j] = x[j], x[i]
                    return


if __name__ == '__main__':
    arr = [1, 44, 21, 33, 12, 90]
    sort_almost_sorted(arr)
    print arr
