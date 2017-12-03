# -*- coding: utf-8 -*-
"""
    从1到n整数中1出现的次数
    ~~~~~~~~~~~~~~~~~~~~~~
    输入一个整数n，求从1到n这n个整数的十进制表示中1出现的次数。
    例如输入12，从1到12这些整数中包含1 的数字有1，10，11和12，1一共出现了5次。
    ~~~~~~~~~~~~~~~~~~~~~~
    https://leetcode.com/problems/number-of-digit-one/solution/
"""


# 方法一：Time complexity: O(n*log(n))
def count_digit_one(n):
    counter = 0
    for i in range(1, n+1):
        string = str(i)
        counter += string.count('1')
    return counter


# 方法二
def count_digit_one2(n):
    def number_of_one(m):
        numbers = 0
        while m:
            if m % 10 == 1:
                numbers += 1
            m //= 10
        return numbers
    counter = 0
    for i in range(1, n+1):
        counter += number_of_one(i)
    return counter


# 方法三
def count_digit_one3(n):
    i = 1
    counter = 0
    while i <= n:
        divider = i * 10
        counter += (n//divider) * i + min(max(n % divider - i + 1, float('-inf')), i)  # noqa
        i *= 10
    return counter


if __name__ == '__main__':
    rv = count_digit_one(21345)
    rv2 = count_digit_one2(21345)
    rv3 = count_digit_one3(21345)
    assert rv == 18821, 'Result {} not expect 18821'.format(rv)
    assert rv2 == 18821, 'Result {} not expect 18821'.format(rv)
    assert rv3 == 18821, 'Result is {} not expcect 18821'.format(rv3)
