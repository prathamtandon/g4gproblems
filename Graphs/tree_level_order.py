from collections import deque
"""
Level order traversal of binary tree.
"""

"""
Approach:
1. We count the number of nodes at each level.
2. We use a queue to store the nodes.
3. Keep printing on same line until all nodes in same level have been printed.

Approach 2:
1. We can use two queues.
2. Insert root in queue1.
3. Repeat while at least one of the queues is not empty.
4. While there are items in queue1, remove the item, print it and add its children to queue2.
5. Print newline.
4. While there are items in queue2, remove the item, print it and add its children to queue1.
"""


def level_order(root):
    queue = deque([root.key])

    while True:
        node_count = len(queue)
        if node_count == 0:
            break

        while node_count > 0:
            node = queue.popleft()
            print node.key,
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            node_count -= 1

        print '\n'


class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right
