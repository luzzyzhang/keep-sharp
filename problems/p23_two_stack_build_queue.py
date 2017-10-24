# -*- coding: utf-8 -*-
"""
    用两个栈实现队列
    ~~~~~~~~~~~~~~~~
    题目：用两个栈实现一个队列。
    请实现它的两个函数append_tail和delete_head，
    分别完成在队列尾部插入结点和在队列头部删除结点的功能。
"""


class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def append_tail(self, x):
        self.stack1.append(x)

    def delete_head(self):
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        head = self.stack2.pop()
        return head


if __name__ == '__main__':
    queue = MyQueue()
    queue.append_tail(1)
    queue.append_tail(2)
    queue.append_tail(3)
    a = queue.delete_head()
    b = queue.delete_head()
    queue.append_tail(4)
    c = queue.delete_head()
    d = queue.delete_head()
    print(a, b, c, d)
