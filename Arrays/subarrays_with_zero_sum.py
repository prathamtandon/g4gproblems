"""
Given an array, print all subarrays in array which has sum 0.
Input:  arr = [6, 3, -1, -3, 4, -2, 2,
             4, 6, -12, -7]
Output:
Subarray found from Index 2 to 4
Subarray found from Index 2 to 6
Subarray found from Index 5 to 6
Subarray found from Index 6 to 9
Subarray found from Index 0 to 10
"""


def subarrays_with_zero_sum(los):
    running_sum = 0
    map = {}
    output = []

    for i in xrange(len(los)):
        running_sum += los[i]
        if running_sum == 0:
            output.append((0, i))
        if running_sum in map:
            for j in map[running_sum]:
                output.append((j + 1, i))
        if running_sum not in map:
            map[running_sum] = [i]
        else:
            map[running_sum].append(i)

    for i in xrange(len(output)):
        print 'Found sum 0 at: ' + str(output[i][0]) + ',' + str(output[i][1])


if __name__ == '__main__':
    los = [6, 3, -1, -3, 4, -2, 2, 4, 6, -12, -7]
    subarrays_with_zero_sum(los)

