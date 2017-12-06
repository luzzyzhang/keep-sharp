# -*- coding: utf-8 -*-
"""
    滑动窗口的最大值
    ~~~~~~~~~~~~~~~
    给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。
    例如，如果输入数组{2, 3, 4, 2, 6, 2, 5, 1}及滑动窗口的大小3，
    那么一共存在6个滑动窗口，它们的最大值分别为{4, 4, 6, 6, 6, 5}
"""

from collections import deque


def max_in_slid_window(array, size):
    queue = deque(maxlen=size)    # 固定长度之双端队列
    for i, num in enumerate(array):
        queue.append(num)
        if len(queue) == 3:
            yield max(queue)


def max_in_slide_window2(array, size):
    queue = deque()
    # max_in_window = []
    for i in range(size):
        while queue and array[i] >= array[queue[-1]]:
            queue.pop()
        queue.append(i)
    for i in range(size, len(array)):
        yield array[queue[0]]
        # max_in_window.append(array[queue[0]])
        while queue and array[i] >= array[queue[-1]]:
            queue.pop()
        if queue and queue[0] <= i-size:
            queue.popleft()
        queue.append(i)
    # max_in_window.append(array[queue[0]])
    # return max_in_window
    yield array[queue[0]]


if __name__ == '__main__':
    array = [2, 3, 4, 2, 6, 2, 5, 1]
    expect = [4, 4, 6, 6, 6, 5]
    rv = list(max_in_slide_window2(array, 3))
    assert rv == expect, 'Invalid result {}'.format(rv)
