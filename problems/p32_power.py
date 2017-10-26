# -*- coding: utf-8 -*-
"""
    数值的整数次方
    ~~~~~~~~~~~~~
    题目：实现函数 power(base: double, exponent: int) -> double:,
          求 base 的 exponent 次方。
    要求：不使用库函数，不考虑大数问题。
"""


def power(base, exponent):
    if base == 0:
        return 0
    if exponent == 0:
        return 1

    result = 1
    abs_exponent = abs(exponent)  # OR abs_exponent = -exponent if exponent < 0 else exponent  # noqa
    while abs_exponent:
        result *= base
        abs_exponent -= 1

    return 1 / result if exponent < 0 else result


# 使用公式，递归法实现
# a^n = a^(n/2) * a^(n/2), n 为偶数；a^n = a^(n-1)/2 * a^(n-1)/2 * a，n 为奇数
# 右移运算替代除以 2，位与运算替代求余（%）运算判断奇偶;提高运算效率
def power_optimize(base, exponent):
    if base == 0:
        return 0
    if exponent == 0:
        return 1
    abs_exponent = abs(exponent)
    result = power_abs_exponent(base, abs_exponent)
    return 1 / result if exponent < 0 else result


# n is non-negative number (n >= 0)
def power_abs_exponent(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    r = power_abs_exponent(a, n >> 1)
    r *= r
    if n & 0x1 == 1:
        r *= a
    return r


if __name__ == '__main__':
    print(power(2, 3))
    print(power(2, -3))
    print(power_optimize(2, 3))
    print(power_optimize(2, -3))
