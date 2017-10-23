# -*- coding: utf-8 -*-

"""
    Longest consecutive characters
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    https://www.youtube.com/watch?v=qRNB8CV3_LU
    s = 'AABCDDBBBEA'
    r = longest_cons_char(s)
    r -> {'B': 3}
"""


def longest_cons_char(s):
    max_char = None
    max_count = 0
    prev_char = None
    count = 0

    for current in s:
        if current == prev_char:
            count += 1
        else:
            count = 1
        if count > max_count:
            max_count = count
            max_char = current
        prev_char = current
    return {max_char: max_count}


if __name__ == '__main__':
    s = 'AABCDDBBBEA'
    r = longest_cons_char(s)
    print(r)
    assert r == {'B': 3}
