# -*- coding: utf-8 -*-
"""
    包含min函数的栈
    ~~~~~~~~~~~~~~
    定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的min
    函数。在该栈中，调用min、push及pop的时间复杂度都是O(1)。
"""


class Stack:

    def __init__(self):
        self.data_stack = []
        self.min_stack = []

    def push(self, value):
        self.data_stack.append(value)
        if len(self.min_stack) == 0 or value < self.min_stack[-1]:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        assert len(self.data_stack) > 0 and len(self.min_stack) > 0
        self.data_stack.pop()
        self.min_stack.pop()

    def min(self):
        assert len(self.data_stack) > 0 and len(self.min_stack) > 0
        return self.min_stack[-1]


if __name__ == '__main__':
    stack = Stack()
    stack.push(3)
    assert stack.min() == 3
    stack.push(4)
    assert stack.min() == 3
    stack.push(2)
    assert stack.min() == 2
    stack.push(1)
    assert stack.min() == 1
    stack.pop()
    assert stack.min() == 2
    stack.pop()
    assert stack.min() == 3
    stack.push(0)
    assert stack.min() == 0
