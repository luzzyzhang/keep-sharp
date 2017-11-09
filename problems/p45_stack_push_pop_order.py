# -*- coding: utf-8 -*-
"""
    栈的压入、弹出序列
    ~~~~~~~~~~~~~~~~~
    输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是
    否为该栈的弹出顺序。假设压入栈的所有数字均不相等。
    例如序列1、2、3、4、5是某栈的压栈序列，
    序列4、5、3、2、1是该压栈序列对应的一个弹出序列，
    但4、3、5、1、2就不可能是该压栈序列的弹出序列。
"""


def is_pop_order(push_lst, pop_lst):
    length = len(push_lst)
    if length == 0:
        return False
    stack = []
    index = 0
    for n in push_lst:
        if n != pop_lst[index]:
            stack.append(n)
        else:
            index += 1
            while (len(stack) != 0) and (stack[-1] == pop_lst[index]):
                stack.pop()
                index += 1
    return len(stack) == 0


if __name__ == '__main__':
    push_lst = [1, 2, 3, 4, 5]
    pop_lst1 = [4, 5, 3, 2, 1]
    pop_lst2 = [4, 3, 5, 1, 2]
    assert is_pop_order(push_lst, pop_lst1) is True
    assert is_pop_order(push_lst, pop_lst2) is False
