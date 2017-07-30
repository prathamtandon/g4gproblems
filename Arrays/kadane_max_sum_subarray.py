def kadane_max_sum_subarray(arr):

    sumVal = 0
    ans = -float('inf')

    for i in range(len(arr)):
        sumVal += arr[i]
        ans = max(ans, sumVal)
        if sumVal < 0:
            sumVal = 0

    return ans


if __name__ == '__main__':
    arr = [2, 3, -5, 9]
    print kadane_max_sum_subarray(arr)
    arr = [-4, -5, -2, -7]
    print kadane_max_sum_subarray(arr)
