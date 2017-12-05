# -*- coding: utf-8 -*-
"""
    (一)：数组中只出现一次的两个数字
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序
    找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
"""


def find_nums_apear_once(array):
    tmp_exclue_or = 0
    for num in array:
        tmp_exclue_or ^= num
    index_of_one = find_first_bit_is_one(tmp_exclue_or)

    num1 = num2 = 0
    for num in array:
        if is_bit_one(num, index_of_one):
            num1 ^= num
        else:
            num2 ^= num
    return {num1, num2}


# 找到num从右边数起第一个是1的位
def find_first_bit_is_one(num):
    index_bit = 0
    while (num & 1 == 0):
        num = num >> 1
        index_bit += 1
    return index_bit


# 判断数字num的第index位是不是1
def is_bit_one(num, index):
    num = num >> index
    return num & 1


if __name__ == '__main__':
    array = [2, 4, 3, 6, 3, 2, 5, 5]
    expect = {4, 6}
    rv = find_nums_apear_once(array)
    assert rv == expect, 'Invalid result {}, expect {}'.format(rv, expect)
