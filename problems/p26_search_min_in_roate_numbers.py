# -*- coding: utf-8 -*-
"""
    旋转数组的最小数字
    ~~~~~~~~~~~~~~~~~
    题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
    输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如数组
    {3, 4, 5, 1, 2}为{1, 2, 3, 4, 5}的一个旋转，该数组的最小值为1。
"""


# 直观解法顺序遍历，时间复杂度 O(n)
def search_min_in_order(numbers):
    min_num = numbers[0]
    for num in numbers:
        if min_num > num:
            min_num = num
    return min_num


# 二分查找，时间复杂度 O(logn)
def search_min_num(numbers):
    left, right = 0, len(numbers) - 1
    mid = left  # 初始化 mid ，如果输入数字没有旋转直接返回第一个元素最小

    while numbers[left] >= numbers[right]:
        if right - left == 1:
            mid = right
            break
        mid = (left+right) // 2
        # 如果 left right mid 三个位置的元素相等只能按顺序查找
        if numbers[left] == numbers[right] == numbers[mid]:
            return search_min_in_order(numbers[left:right+1])

        if numbers[mid] >= numbers[left]:
            left = mid
        elif numbers[mid] <= numbers[right]:
            right = mid

    return numbers[mid]


if __name__ == '__main__':
    numbers = [1, 0, 1, 1, 1]
    numbers2 = [3, 4, 5, 1, 2]
    rv = search_min_in_order(numbers)
    rv2 = search_min_num(numbers2)
    print(rv, rv2)
