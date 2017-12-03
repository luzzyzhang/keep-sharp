# -*- coding: utf-8 -*-
"""
    丑数
    ~~~
    我们把只包含因子2、3和5的数称作丑数（Ugly Number）。
    求按从小到大的顺序的第1500个丑数。
    例如6、8都是丑数，但14不是，因为它包含因子7。
    习惯上我们把1当做第一个丑数。
"""


def get_ugly_numbers(index):
    number = 0
    while index > 0:
        number += 1
        if is_ugly(number):
            index -= 1
    return number


def is_ugly(number):
    while number % 2 == 0:
        number //= 2
    while number % 3 == 0:
        number //= 3
    while number % 5 == 0:
        number /= 5
    return number == 1


# 方法2：空间换时间
def get_ugly_numbers2(index):
    ugly_numbers = [1]
    next_ugly_index = 1
    multi2_index = 0
    multi3_index = 0
    multi5_index = 0

    while next_ugly_index < index:
        min_num = min(ugly_numbers[multi2_index]*2,
                      ugly_numbers[multi3_index]*3,
                      ugly_numbers[multi5_index]*5)
        ugly_numbers.append(min_num)

        while ugly_numbers[multi2_index]*2 <= ugly_numbers[next_ugly_index]:
            multi2_index += 1
        while ugly_numbers[multi3_index]*3 <= ugly_numbers[next_ugly_index]:
            multi3_index += 1
        while ugly_numbers[multi5_index]*5 <= ugly_numbers[next_ugly_index]:
            multi5_index += 1

        next_ugly_index += 1
    return ugly_numbers[index-1]


if __name__ == '__main__':
    rv = get_ugly_numbers(10)
    expect = 12
    assert rv == expect, '{} != {}'.format(rv, expect)
    rv2 = get_ugly_numbers2(1500)
    expect2 = 859963392
    assert rv2 == expect2, '{} != {}'.format(rv2, expect2)
