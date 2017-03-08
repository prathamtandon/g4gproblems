import heapq
"""
Given that integers are read from a data stream, find the median of elements read so far
in efficient way. For example, consider the stream: 5 15 1 3...
After reading first element of stream, median is 5
After reading 2nd element of stream, median is 10
After reading 3rd element of stream, median is 5
After reading 4th element of stream, median is 4
"""

"""
Approach:
1. Idea is to use a MaxHeap to hold all elements which are to the left of effective median.
2. Use a MinHeap to hold all elements which are to the right of effective median.
3. If both heaps have same number of elements, then effective median is average of the roots of the two heaps.
4. Otherwise, heaps with differ in size by at most 1, and effective median is root of heap containing the larger
   number of elements.
"""


def median_stream_ints(arr):

    less_than_med = []
    greater_than_med = []

    for i in range(len(arr)):
        print 'Median after adding:', arr[i]
        if len(less_than_med) == 0 and len(greater_than_med) == 0:
            heapq.heappush(less_than_med, -arr[i])  # max-heap in Python implemented by negation.
        elif arr[i] < abs(less_than_med[0]):
            heapq.heappush(less_than_med, -arr[i])
            if len(less_than_med) - len(greater_than_med) > 1:
                root = abs(heapq.heappop(less_than_med))
                heapq.heappush(greater_than_med, root)
        elif len(greater_than_med) == 0 or arr[i] > greater_than_med[0]:
            heapq.heappush(greater_than_med, arr[i])
            if len(greater_than_med) - len(less_than_med) > 1:
                root = heapq.heappop(greater_than_med)
                heapq.heappush(less_than_med, -root)
        if len(less_than_med) == len(greater_than_med):
            print (greater_than_med[0] - less_than_med[0]) / 2
        else:
            print abs(less_than_med[0]) if len(less_than_med) > len(greater_than_med) else greater_than_med[0]


if __name__ == '__main__':
    median_stream_ints([5, 15, 1, 3])
