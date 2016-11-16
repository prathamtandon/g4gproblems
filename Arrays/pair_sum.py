import unittest

"""
Given an array A[] and a number x, check for pair in A[] with sum as x.
input: [12,-3,4,7,11], x = 8
output: ele1 = -3, ele2 = 11
"""

"""
Approach 1:
1. Sort the input array
2. initialize left = 0 and right = len(array)-1
3. while left <= right,
4. if a[left] + a[right] = x, return a[left],a[right]
5. else move the pointers appropriately.
6. We can also do a binary search - chose an element, then do a BS for x-element in the array.
"""


def pair_sum_using_sort(list_of_nums, desired_sum):
    list_of_nums.sort()
    left = 0
    right = len(list_of_nums) - 1
    while left <= right:
        left_val = list_of_nums[left]
        right_val = list_of_nums[right]
        sum_val = left_val + right_val
        if sum_val == desired_sum:
            return left_val, right_val
        elif sum_val < desired_sum:
            left += 1
        else:
            right -= 1

    return None

"""
Approach 2:
1. Initialize a dictionary D
2. Loop over the input list
3. If (x-ele) is in D, return ele and x-ele
4. Insert ele in D
5. Linear runtime with extra storage
"""


def pair_sum_using_dict(list_of_nums, desired_sum):
    symbol_table = dict()
    for num in list_of_nums:
        other = desired_sum - num
        if other in symbol_table:
            return num, other
        else:
            symbol_table[num] = None

    return None


class TestPairSum(unittest.TestCase):

    def test_pair_sum_using_sort(self):
        arr = [1, 4, 45, 6, 10, -8]
        x = 16

        ele1, ele2 = pair_sum_using_sort(arr, x)
        self.assertEqual(ele1, 6)
        self.assertEqual(ele2, 10)

    def test_pair_sum_using_dict(self):
        arr = [1, 4, 45, 6, 10, -8]
        x = 16

        ele1, ele2 = pair_sum_using_dict(arr, x)
        self.assertEqual(ele1, 10)
        self.assertEqual(ele2, 6)


if __name__ == '__main__':
    unittest.main()



