import unittest
"""
Given a set of n nuts of different sizes and n bolts of different sizes, there is a one-one mapping between
nuts and bolts. Match nuts and bolts efficiently.
Constraint: Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means nut can
only be compared with a bolt and bolt can only be compared with nut to see which one is bigger/smaller.

Another way to ask the same question: We have a box of locks and keys where one lock can be opened by one key
in the box. We need to match the pair.
"""

"""
Approach:
1. Use quick sort technique to solve this.
2. First, perform a partition by picking last element of bolts array as pivot.
3. Rearrange the array of nuts and returns the partition index 'i' such that all nuts smaller than nuts[i]
   are on the left side and all nuts greater than nuts[i] are on the right side.
4. Next using nuts[i] as pivot, partition the array of bolts.
5. Apply partitioning recursively on the left and right sub-arrays of nuts and bolts.
6. The total time complexity is O(2*nlogn) = O(nlogn).
"""


def nuts_and_bolts_match(nuts, bolts):

    assert len(nuts) == len(bolts)
    match_pairs(nuts, bolts, 0, len(nuts)-1)


def match_pairs(nuts, bolts, low, high):

    if low < high:
        pivot_index = partition(nuts, low, high, bolts[high])
        partition(bolts, low, high, nuts[pivot_index])
        match_pairs(nuts, bolts, low, pivot_index-1)
        match_pairs(nuts, bolts, pivot_index+1, high)


def partition(loi, low, high, pivot):
    """
    Unlike usual partition, we are passing pivot element as an argument to partition.
    Hence, the additional check for array element being equal to pivot.
    """
    i = low
    for j in range(low, high-1):
        if loi[j] < pivot:
            loi[i], loi[j] = loi[j], loi[i]
            i += 1
        elif loi[j] == pivot:
            loi[j], loi[high] = loi[high], loi[j]
            j -= 1
    loi[i], loi[high] = loi[high], loi[i]
    return i


class TestNutsAndBoltsMatching(unittest.TestCase):

    def test_nuts_and_bolts(self):
        nuts = ['@', '#', '$', '%', '^', '&']
        bolts = ['$', '%', '&', '^', '@', '#']

        nuts_and_bolts_match(nuts, bolts)
        self.assertEqual(nuts, ['#', '$', '%', '&', '@', '^'])
        self.assertEqual(bolts, ['#', '$', '%', '&', '^', '@'])
