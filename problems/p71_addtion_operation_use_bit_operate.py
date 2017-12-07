# -*- coding: utf-8 -*-
"""
"""


def add(num1, num2):
    sum_, carry = 0, 0
    while num2 != 0:
        sum_ = num1 ^ num2
        carry = (num1 & num2) << 1

        num1 = sum_
        num2 = carry
    return num1


if __name__ == '__main__':
    print(add(11, 22))
    assert add(11, 22) == 33
