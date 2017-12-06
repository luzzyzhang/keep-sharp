# -*- coding: utf-8 -*-
"""
    队列的最大值
    ~~~~~~~~~~~
    定义队列并实现max方法得到队列之最大值，
    要求push_back, pop_front 时间复杂度都是 O(1)
"""

from collections import deque, namedtuple

InternalData = namedtuple('InternalData', 'value, index')


class MaxQueue:
    def __init__(self):
        self.data = deque()
        self.max_nums = deque()
        self.index = 0

    def __repr__(self):
        return '<MaxQueue: data={}, max_nums={}>'.format(self.data.val, self.max_nums)  # noqa

    def push_back(self, val):
        while self.max_nums and val >= self.max_nums[-1].value:
            self.max_nums.pop()
        inter_data = InternalData(val, self.index)
        self.data.append(inter_data)
        self.max_nums.append(inter_data)
        self.index += 1

    def pop_front(self):
        if not self.max_nums:
            raise IndexError('pop from an empty deque')
        if self.max_nums[0].index == self.data[0].index:
            self.max_nums.popleft()
        return self.data.popleft().value

    def get_max(self):
        if not self.max_nums:
            raise IndexError('empty deque')
        return self.max_nums[0].value


if __name__ == '__main__':
    max_queue = MaxQueue()
    max_queue.push_back(7)
    max_queue.push_back(2)
    max_queue.push_back(3)
    max_queue.push_back(4)
    print(max_queue.get_max())
    print(max_queue.pop_front())
    print(max_queue.get_max())
