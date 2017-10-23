# -*- coding: utf-8 -*-
"""
   Fibonacci数列
"""


# ===== 求第n项 ========

# 循环法
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# 递归法，效率比较差，大量重复计算
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)


# ====== 获取 fibonacci 数列 ========

def fibs_iter(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    fibonaccis_array = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    assert fib_iter(8) == 21
    assert fib_recursive(8) == 21

    assert list(fibs_iter(8)) == fibonaccis_array[:-1]
    # assert list(fibs_recursive(8)) == fibonaccis_array[:-1]
