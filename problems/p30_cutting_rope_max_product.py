# -*- coding: utf-8 -*-
"""
    剪绳子
    题目：给你一根长度为n绳子，请把绳子剪成m段（m、n都是整数，n>1并且m≥1）。
    每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]*k[1]*…*k[m]可能的最大乘
    积是多少？例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此
    时得到最大的乘积18。
    ~~~~~~~~~~~~~~~~~~~~~~
    类似问题找零钱问题
"""


# 动态规划解法: 时间复杂度O(n^2), 空间复杂度O(n)
def max_product_dynamic(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2
    products = [0, 1, 2, 3] + [0 for _ in range(length-3)]
    max_product = 0

    for i in range(4, length+1):
        for j in range(1, (i//2)+1):
            max_product = max(max_product, products[j]*products[i-j])
        products[i] = max_product
    return products[length]


# 贪心算法: 时间复杂度 O(1), 空间复杂度 O(1), 贪心算法需要数学证明
def max_product_greedy(length):
    if length < 2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    times_of_3 = length // 3
    if length - 3*times_of_3 == 1:
        times_of_3 -= 1
    times_of_2 = (length - 3*times_of_3) // 2

    return (3**times_of_3) * (2**times_of_2)


if __name__ == '__main__':
    print(max_product_dynamic(7))
    print(max_product_greedy(7))
