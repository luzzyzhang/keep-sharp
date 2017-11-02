# -*- coding: utf-8 -*-
"""
    表示数值的字符串
    ~~~~~~~~~~~~~~~
    题目：请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
    例如，字符串"+100"、"5e2"、"-123"、"3.1416"及"-1E-16"都表示数值，
    但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是
"""

from unicodedata import numeric


# 数字的格式可以用A[.[B]][e|EC]或者.B[e|EC]表示，其中A和C都是
# 整数（可以有正负号，也可以没有），而B是一个无符号整数


# ---------- Use Flags and iterate string ---------- #
def is_numeric(string):
    number = False
    e = False
    point = False
    number_after_e = True
    for index, char in enumerate(string):
        if '0' <= char <= '9':
            number = True
            number_after_e = True
        elif char == '.':
            if e or point:
                return False
            point = True
        elif char == 'e' or char == 'E':
            if e or not number:
                return False
            number_after_e = False
            e = True
        elif char == '-' or char == '+':
            if index != 0 and string[index-1] not in {'e', 'E'}:
                return False
        else:
            return False
    return number and number_after_e


# ---------- 犯规解法😄  ---------- #
def isnumeric(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


if __name__ == '__main__':
    # assert isnumeric('abc') is False
    # assert isnumeric('-1.3') is True
    # assert isnumeric('.3') is True
    # assert isnumeric('四') is True
    # assert is_numeric('-1.3') is True
    # assert is_numeric('.3') is True
    # assert is_numeric('abc') is False
    print(is_numeric('1.2.3'))
