"""
Given two sorted linked lists, merge them such the overall list is sorted in increasing order.
Return the head of the new list. Expected space complexity us O(1) i.e. no new nodes should be created.
"""


"""
Approach:
1. Simple approach is to have two pointers, say L1 and L2.
2. Let head always point to start of list with first smaller item, and L1 always point to list with first smaller
   item and L2 always point to the other list.
3. If L1.data < L2.data, we just move L1 to next node.
4. However, if L1.data > L2.data, we need to insert L2 into L1 such that L1 still remains sorted.
5. To summarize, we will be using L1 as the target list. If last element in L1 is not the overall largest,
   we will set L1 point to L2.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_sorted_lists(LL1, LL2):
    if not LL1:
        return LL2
    if not LL2:
        return LL1

    result = LL1 if LL1.data < LL2.data else LL2
    other = LL1 if result is LL2 else LL2
    cur = result

    while cur.next and other:
            if cur.next.data > other.data:
                    temp = other
                    other = other.next
                    temp.next = cur.next
                    cur.next = temp
            cur = cur.next

    if other:
        cur.next = other

    return result


def insert_between(left, right, node):
    if left:
        left.next = node
    node.next = right


def print_ll(head):
    result = []
    temp = head
    while temp:
        result.append(temp.data)
        temp = temp.next
    print result


if __name__ == '__main__':
    head1 = Node(3)
    head1.next = Node(6)
    head1.next.next = Node(7)

    head2 = Node(1)
    head2.next = Node(2)
    head2.next.next = Node(5)
    head2.next.next.next = Node(8)

    print_ll(head1)
    print_ll(head2)
    print_ll(merge_sorted_lists(head1, head2))

