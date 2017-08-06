from random import random
"""
Given an array, write a program to generate a random permutation of array elements.
"""

"""
Approach 1:
1. Create a list of indices 0...n-1.
2. Select a random index from the list.
3. Take element in array at the selected index and append it to output.
4. Delete the index from the list and repeat.
T.C: O(n^2)
S.C: O(n)
"""


"""
NOTE: This is the approach used in Python standard library function "shuffle"
Approach 2: (Fisher-Yates shuffle algorithm)
ASSUME: We have a function rand() that generates a random number in O(1) time.
1. Traverse the array from right to left.
2. For current index i, generate a random number between 0 and i INCLUSIVE. Let it be j.
3. Swap arr[i] and arr[j].

Prob of element at index i ending at index n-1 = 1/n (each value equally likely)
Prob of element at index i ending at index n-2 = Prob it does not end at n-1 * Prob it ends at n-2
= (n-1)/n * 1/(n-1) = 1/n
Likewise, we can show that for every element, probability of ending up at any position, including current
position is 1/n.
"""


def shuffle(x):

    for i in reversed(xrange(1, len(x))):
        # Select a random value in x[:i+1] with which to exchange x[i]
        j = int(random() * (i + 1))
        x[i], x[j] = x[j], x[i]


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    shuffle(arr)
    print arr



