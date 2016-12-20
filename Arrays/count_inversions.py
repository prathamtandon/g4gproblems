import unittest
"""
Inversion Count for an array indicates - how far (or close) the array is from being sorted.
If array is already sorted, then inversion count is 0. If array is sorted in reverse order,
then inversion count is maximum.
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
Input: 2 4 1 3 5
Output: 3 inversions: (2,1) (4,1) (4,3)
"""

"""
Approach 1 (Enhanced MergeSort)
1. Suppose we know the number of inversions in left half and right half of array.
2. Apart from these, we need to count - how many inversions happen during merge step.
3. During merge, suppose a[i] is current element in left section, and a[j] is current element in right section.
4. If mid represents middle index and a[i] > a[j], then there are mid - i inversions.
5. This is because all elements from a[i+1...mid-1] are greater than a[i] and hence greater than a[j].
6. Time complexity is O(nlogn) and space complexity is O(n).
"""


def count_inversions(list_of_numbers):
    end = len(list_of_numbers)
    temp = [0] * end
    return merge_sort(list_of_numbers, temp, 0, end - 1)


def merge_sort(list_of_numbers, temp, low, high):
    num_inversions = 0
    if low < high:
        mid = low + (high - low) / 2
        num_inversions += merge_sort(list_of_numbers, temp, low, mid)
        num_inversions += merge_sort(list_of_numbers, temp, mid + 1, high)
        num_inversions += merge(list_of_numbers, temp, low, mid+1, high)
    return num_inversions


def merge(list_of_numbers, temp, low, mid, high):
    i = low
    j = mid
    k = low
    inversion_count = 0

    while i < mid and j <= high:
        if list_of_numbers[i] <= list_of_numbers[j]:
            temp[k] = list_of_numbers[i]
            i += 1
            k += 1
        else:
            temp[k] = list_of_numbers[j]
            k += 1
            j += 1
            inversion_count += (mid - i)

    while i < mid:
        temp[k] = list_of_numbers[i]
        k += 1
        i += 1

    while j <= high:
        temp[k] = list_of_numbers[j]
        k += 1
        j += 1

    for i in range(low, high+1):
        list_of_numbers[i] = temp[i]

    return inversion_count


class TestInversionCount(unittest.TestCase):

    def test_inversion_count(self):
        list_of_numbers = [1, 20, 6, 4, 5]
        self.assertEqual(count_inversions(list_of_numbers), 5)
