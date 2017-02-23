"""
Design and implement methods of an LRU cache. There are two methods defined as follows:
get(x): Gets the value of the key x if the key exists in the cache, otherwise returns -1.
set(x,y): Inserts the value if the key x is not already present. If the cache reaches its capacity, it should
invalidate the least recently used item before inserting the new item.
In the constructor of the class, the capacity of cache needs to be initialized.
"""

"""
Approach:
1. We will utilize two data structures to implement the LRU cache.
2. Firstly, we will need a Queue to store the actual data associated with each key. It will be implemented
   as a doubly linked list. One important feature of the Queue will be that the most recently used items
   will be near the front and the least recently used items will be near the rear end.
3. Secondly, we will use a Hashtable to store the keys. The values will be pointers to corresponding nodes
   in the Queue.
4. After each get/set, the corresponding node will be moved to front of queue and corresponding Hashtable entry
   updated. Also, when max capacity is reached, we will delete the last entry from the Queue and corresponding
   entry from Hashtable.
5. This will give O(1) time complexity for both get and set operations.
"""


class Node:
    def __init__(self, key, data, after=None, before=None):
        self.key = key
        self.data = data
        self.after = after
        self.before = before


class DLLQueue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, key, value):
        node = Node(key, value)
        if self.size == 0:
            self.front = node
            self.rear = node
        else:
            self.front.before = node
            node.after = self.front
            self.front = node
        self.size += 1
        return node

    def dequeue(self):
        if self.size == 0:
            return
        key = self.rear.key
        if self.size == 1:
            self.front = None
            self.rear = None
        else:
            self.rear = self.rear.before
            self.rear.after = None
        self.size -= 1
        return key

    def move_to_front(self, node):
        if self.front is node:
            return
        if self.rear is node:
            self.rear = self.rear.before
        if node.after is not None:
            node.after.before = node.before
        node.before.after = node.after
        self.front.before = node
        node.after = self.front
        node.before = None
        self.front = node


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = {}
        self.queue = DLLQueue()

    def get(self, key):
        if key not in self.table:
            return -1
        node = self.table[key]
        self.queue.move_to_front(node)
        return node.data

    def is_full(self):
        return self.capacity == self.queue.size

    def is_empty(self):
        return self.queue.size == 0

    def set(self, key, value):
        if key not in self.table:
            if self.is_full():
                old = self.queue.dequeue()
                del self.table[old]
            self.table[key] = self.queue.enqueue(key, value)
        else:
            node = self.table[key]
            self.queue.move_to_front(node)
            node.data = value

    def size(self):
        return self.queue.size


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.set(1, 2)
    cache.set(2, 3)
    cache.set(1, 5)
    cache.set(4, 5)
    cache.set(6, 7)
    print cache.get(4)
    print cache.get(1)
