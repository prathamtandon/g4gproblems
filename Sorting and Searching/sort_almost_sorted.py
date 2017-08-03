"""
Given an almost sorted array where only two elements are swapped, how to sort the array efficiently.
"""


def sort_almost_sorted(arr):
    n = len(arr)

    for i in range(n-1, 0, -1):
        if arr[i] < arr[i-1]:
            j = i - 1
            while j >= 0 and arr[j] > arr[i]:
                j -= 1
            arr[i], arr[j+1] = arr[j+1], arr[i]
            break


if __name__ == '__main__':
    arr = [1, 5, 3]
    sort_almost_sorted(arr)
    print arr
