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


if __name__ == '__main__':
    print(power(2, 3))
    print(power(2, -3))
