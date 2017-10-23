# -*- coding: utf-8 -*-

"""
    数组中重复的数字
    ~~~~~~~~~~~~~~~~
    找出数组中重复的数字：在长度为 n 的数组里所有数字都在 0 ～ n-1 的范围内。
    数组中某数字是重复的，但不知道有几个数字重复，也不知道每个数字重复了多少次。
    请找出数组中任意一个重复的数字。
    例如：如果输入长度为 7 的数组 [2, 3, 1, 0, 2, 5, 3] 输出重复数字 2 或 3 。
"""


# 诡异的思路
def duplicate(numbers, n):
    for num in numbers:
        if num < 0 or num > n:
            return []
    for i in range(n):
        while numbers[i] != i:
            if numbers[i] == numbers[numbers[i]]:
                return numbers[i]
            tmp = numbers[i]
            numbers[i] = numbers[tmp]
            numbers[tmp] = tmp
    return []


# 直观思路：遍历数组并使用集合记录
def duplicate2(numbers, n):
    seen = set()
    for num in numbers:
        if num in seen and num > 0 and num <= n:
            yield num
        seen.add(num)


if __name__ == '__main__':
    numbers = [2, 3, 1, 0, 2, 5, 3]
    r = duplicate(numbers, len(numbers))
    print(r)
    print(set(duplicate2(numbers, len(numbers))))
