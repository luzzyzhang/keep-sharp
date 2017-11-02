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
# def isnumberic(string):
#     if not string:
#         return False
# 
#     numeric = scan_integer(string)
#     for index, char in enumerate(string):
# 
#     
# def scan_integer(string):
#     if string[0] == '+' or string[0] == '-':
#         string = string[1:]
#     for char in string:
#         if char >= '0' and char <= '9':
#             return True
#     return False



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
    assert isnumeric('abc') is False
    assert isnumeric('-1.3') is True
    assert isnumeric('.3') is True
    assert isnumeric('四') is True
