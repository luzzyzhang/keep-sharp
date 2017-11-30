# -*- coding: utf-8 -*-
"""
    Find median from data stream.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    https://leetcode.com/problems/find-median-from-data-stream/description/
"""


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


if __name__ == '__main__':
    obj = MedianFinder()
    obj.add_num(1)
    print(obj.find_median())
    obj.add_num(2)
    print(obj.find_median())
    obj.add_num(3)
    print(obj.find_median())
    obj.add_num(4)
    print(obj.find_median())
