"""
Given a list of numbers where every number appears 3 times, except one which only occurs once. Find that number
"""

"""
NICE!
Approach:
1. We find the sum of bits at each position in all the numbers MOD 3.
2. The result of this will be the bit value of single occurrence number at that position.
3. Repeat for all 32 bits to find the single occurrence number.
"""


def get_single(arr):

    iters = 32
    single = 0
    for i in range(iters):
        sum = 0
        for j in range(len(arr)):
            if arr[j] & (1 << i) > 0:
                sum += 1
        sum %= 3
        if sum == 1:
            single += 2 ** i

    return single


if __name__ == '__main__':
    print get_single([5, 5, 5, 7])
    print get_single([12, 3, 3, 1, 12, 3, 1, 2, 1, 12])

