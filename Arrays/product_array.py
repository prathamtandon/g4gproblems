import unittest
"""
Given an array of integers arr, create a product array prod such that
prod[i] = product of (arr[0...n-1] except arr[i]) without using division operator
Input: 10 3 5 6 2
Output: 180 600 360 300 900
"""

"""
Approach:
1. Compute the product of all elements, say all_product
2. For each a[i] find a[i] * all_product, say scaled_all_product
3. Reduce a[i] ** 2 from scaled_all_product one at a time and count how many times we reduce, say count.
4. Right before it becomes zero, return count.
"""


def product_puzzle(list_of_numbers):
    list_product = reduce((lambda x, y: x * y), list_of_numbers)
    products = []

    for num in list_of_numbers:
        scaled_list_product = list_product * num
        partial_product = 1
        while scaled_list_product - num ** 2 != 0:
            scaled_list_product -= num ** 2
            partial_product += 1
        products.append(partial_product)

    return products


class TestProductPuzzle(unittest.TestCase):

    def test_product_puzzle(self):
        list_of_numbers = [10, 3, 5, 6, 2]
        self.assertEqual(product_puzzle(list_of_numbers), [180, 600, 360, 300, 900])


if __name__ == '__main__':
    unittest.main()
