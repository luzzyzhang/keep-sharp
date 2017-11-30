# -*- coding: utf-8 -*-
"""
    Find median from data stream.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    https://leetcode.com/problems/find-median-from-data-stream/description/
"""

from heapq import heappush, heappop


class MedianFinder:
    """Approach 1:
    Store the numbers in a resize-able container.
    Every time you need to output the median,
    sort the container and output the median.

    * Time complexity: O(n*log(n))
    * Space complexity: O(n)
    """

    def __init__(self):
        """Initialize data structure here.
        """
        self.store = []

    def add_num(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.store.append(num)

    def find_median(self):
        """
        :rtype: float
        """
        self.store.sort()
        n = len(self.store)
        return self.store[n//2] if n & 1 else (self.store[n//2 - 1] + self.store[n//2])*0.5


class MedianFinder2:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def add_num(self, num):
        heappush(self.max_heap, -num)
        heappush(self.min_heap, abs(self.max_heap[0]))
        heappop(self.max_heap)

        if len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -self.min_heap[0])
            heappop(self.min_heap)

    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return abs(self.max_heap[0])
        else:
            return (abs(self.min_heap[0]) + abs(self.max_heap[0]))*0.5


if __name__ == '__main__':
    # obj = MedianFinder()
    obj = MedianFinder2()
    obj.add_num(1)
    print(obj.find_median())
    obj.add_num(2)
    print(obj.find_median())
    obj.add_num(3)
    print(obj.find_median())
    obj.add_num(4)
    print(obj.find_median())
    obj.add_num(5)
    print(obj.find_median())
