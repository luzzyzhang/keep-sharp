# -*- coding: utf-8 -*-
"""
    字符串中第一个只出现一次的字符
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    在字符串中找出第一个只出现一次的字符。如输入"abaccdeff"，则输出'b'。
"""


def first_no_repeat_char(string):
    records = {}
    for char in string:
        if char in records:
            records[char] += 1
        else:
            records[char] = 1
    for char in string:
        if records[char] == 1:
            return char


if __name__ == '__main__':
    assert first_no_repeat_char('google') == 'l'
