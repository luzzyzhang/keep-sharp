# -*- coding: utf-8 -*-
"""
   两个队列实现一个栈
"""

from collections import deque


class Stack:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    # efficent push version
    def push(self, val):
        self.queue1.append(val)

    def pop(self):
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        if len(self.queue1) == 1:
            r = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return r

    # efficient pop version
    # def push2(self, val):
    #     self.queue2.append(val)
    #     while self.queue2:
    #         self.queue1.append(self.queue2.popleft())
    #     self.queue1, self.queue2 = self.queue2, self.queue1

    # def pop2(self):
    #     if self.queue1:
    #         d = self.queue1.popleft()


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    a = stack.pop()
    b = stack.pop()
    stack.push(4)
    c = stack.pop()
    e = stack.pop()
    print(a, b, c, e)
