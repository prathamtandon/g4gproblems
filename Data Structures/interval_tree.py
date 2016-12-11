"""
http://www.geeksforgeeks.org/interval-tree/

Search:
1. Compare with root: if overlap with root, return root.
2. Compare with root.left: if root.left is not None and root.left.max >= interval.low, search root.left
3. Else search root.right.
"""


class IntervalTree:

    class Interval:
        def __init__(self, low, high):
            self.low = low
            self.high = high

    class Node:
        def __init__(self, interval, max):
            self.interval = interval
            self.max = max
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert_helper(self, node, interval):
        if node is None:
            return IntervalTree.Node(interval, interval.high)
        low = node.interval.low
        high = node.interval.high

        if interval.low < low:
            node.left = self.insert_helper(node.left, interval)
        else:
            node.right = self.insert_helper(node.right, interval)

        node.max = max(node.max, high)
        return node

    def insert(self, interval):
        self.root = self.insert_helper(self.root, interval)

    def intervals_overlap(self, interval1, interval2):
        if interval1.high < interval2.low or interval2.high < interval1.low:
            return False
        return True

    def overlap_search(self, interval):
        return self.overlap_search_helper(self.root, interval)

    def overlap_search_helper(self, node, interval):
        if node is None:
            return None
        if self.intervals_overlap(node.interval, interval):
            return node.interval
        if node.left is not None and interval.low <= node.left.max:
            return self.overlap_search_helper(node.left, interval)
        else:
            return self.overlap_search_helper(node.right, interval)


if __name__ == '__main__':
    intervals = [IntervalTree.Interval(15, 20),
                 IntervalTree.Interval(10, 30),
                 IntervalTree.Interval(17, 19),
                 IntervalTree.Interval(5, 20),
                 IntervalTree.Interval(12, 15),
                 IntervalTree.Interval(30, 40)]
    interval_tree = IntervalTree()
    for interval in intervals:
        interval_tree.insert(interval)

    interval = IntervalTree.Interval(6, 7)
    overlapping_interval = interval_tree.overlap_search(interval)

    if overlapping_interval is None:
        print 'No overlapping interval found.'
    else:
        print '[', overlapping_interval.low, ',', overlapping_interval.high, ']'
