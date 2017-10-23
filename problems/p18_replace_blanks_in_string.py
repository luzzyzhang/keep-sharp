# -*- coding: utf-8 -*-
"""
    替换空格
    ~~~~~~~
    题目：请实现一个函数，把字符串中的每个空格替换成"%20"。
    例如输入“We are happy.”，则输出“We%20are%20happy.”。
"""


def replace_space(string, length):
    if not string or length <= 0:
        return string

    origin_len, space_num = 0, 0
    for s in string:
        origin_len += 1
        if s.isspace():
            space_num += 1

    # new_len 空格替换为 %20 之后的长度
    new_len = origin_len + space_num * 2
    if new_len > length:
        return None

    index_origin = origin_len
    index_new = new_len
    string = list(string) + ['' for _ in range(new_len)]  # 空间足够

    while (index_origin >= 0 and index_new > index_origin):
        if string[index_origin].isspace():
            string[index_new] = '0'
            string[index_new-1] = '2'
            string[index_new-2] = '%'
            index_new -= 3
        else:
            string[index_new] = string[index_origin]
            index_new -= 1

        index_origin -= 1
    return ''.join(string)


def replace_space2(string):
    return string.replace(' ', '%20')


if __name__ == '__main__':
    string = 'We are happy.'
    rv = replace_space(string, 50)
    print(rv)
