def kadane_max_sum_subarray(arr):
    n = len(arr)
    # dp[i] denotes the max sum value for arr[0...i]
    # At each element, we decide either to leverage to running sum so far, or start a new subarray.
    dp = [0] * n
    sumVal = 0
    for i in range(n):
        sumVal += arr[i]
        dp[i] = max(sumVal, arr[i])
        sumVal = max(sumVal, 0)

    return max(dp)


if __name__ == '__main__':
    arr = [2, 3, -5, 9]
    print kadane_max_sum_subarray(arr)
    arr = [-4, -5, -2, -7]
    print kadane_max_sum_subarray(arr)
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print kadane_max_sum_subarray(arr)
