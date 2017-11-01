"""
Convert binary tree to its mirror in-place.
"""


def convert_to_mirror(node):
    if not node:
        return

    # convert left and right subtrees to their respective mirrors
    convert_to_mirror(node.left)
    convert_to_mirror(node.right)

    # swap left and right links
    node.left, node.right = node.right, node.left
