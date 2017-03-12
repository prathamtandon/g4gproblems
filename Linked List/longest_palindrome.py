import unittest
"""
Given a linked list, find length of the longest palindrome list that exists in that linked list.
Expected space complexity is O(1).
Input: 2->3->7->3->2->12->24
Output: 5
Input: 12->4->5->4->3->14
Output: 3
Input: 2->3->3->2
Output: 4
"""

"""
Approach:
1. We use the iterative method to reverse a linked list.
2. We start reversing all N prefixes of the linked list one by one.
3. Each reversed prefix is compared with remaining linked list till characters match.
4. Compare for both even and odd length palindromes by including current node as well as excluding current node
   while comparing.
5. Update the max length as needed.
"""


def max_palidromic(head):
    prev = None
    cur = head
    result = 0

    while cur:
        next = cur.next
        cur.next = prev

        # Case where current node is middle in odd length palindrome
        result = max(result, 2 * count_common(prev, next) + 1)

        # Case where current node is not middle in even length palindrome
        result = max(result, 2 * count_common(cur, next))

        prev = cur
        cur = next

    # If modifications are not allowed, we can do reverse(head) to get back original
    return result


def count_common(a, b):
    count = 0
    while a and b and a.data == b.data:
        count += 1
        a = a.next
        b = b.next
    return count


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class TestLongestPalin(unittest.TestCase):

    def test_longest_palin(self):
        head = Node(2)
        head.next = Node(3)
        head.next.next = Node(5)
        head.next.next.next = Node(3)
        head.next.next.next.next = Node(2)
        head.next.next.next.next.next = Node(21)
        head.next.next.next.next.next.next = Node(24)

        self.assertEqual(max_palidromic(head), 5)

        head = Node(2)
        head.next = Node(4)
        head.next.next = Node(5)
        head.next.next.next = Node(5)
        head.next.next.next.next = Node(4)

        self.assertEqual(max_palidromic(head), 4)

        head = Node(2)
        head.next = Node(4)

        self.assertEqual(max_palidromic(head), 1)
