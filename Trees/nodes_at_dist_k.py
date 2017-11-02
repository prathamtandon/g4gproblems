"""
Print all nodes at distance k from given node in a binary tree.
"""


def print_k_distance_down(node, k):
    if not node or k < 0:
        return
    if k == 0:
        print node.data
        return
    print_k_distance_down(node.left, k - 1)
    print_k_distance_down(node.right, k - 1)


def print_nodes_at_distance(node, target, k):
    if not node:
        return -1
    if node is target:
        print_k_distance_down(node, k)
        return 0
    dl = print_nodes_at_distance(node.left, target, k)

    if dl != -1:
        if dl + 1 == k:
            print node.data
        else:
            print_k_distance_down(node.right, k - dl - 2)
        return 1 + dl

    dr = print_nodes_at_distance(node.right, target, k)

    if dr != -1:
        if dr + 1 == k:
            print node.data
        else:
            print_k_distance_down(node.left, k - dr - 2)
        return 1 + dr

    return -1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    print_nodes_at_distance(root, root.left.right, 2)


