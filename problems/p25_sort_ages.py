# -*- coding: utf-8 -*-
"""
    实现一排序算法，要求事件复杂度O(n)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    条件：某企业有数万名员工，按年龄排序
"""


def sort_ages(ages):
    oldest_age = 100
    times_of_age = [0 for _ in range(oldest_age)]
    for age in ages:
        times_of_age[age] += 1

    index = 0
    for i in range(oldest_age):
        for _ in range(times_of_age[i]):
            ages[index] = i
            index += 1

    return ages


if __name__ == '__main__':
    from random import randrange
    ages = [randrange(0, 100) for _ in range(20)]
    print(ages)
    sorted_arges = sort_ages(ages)
    print(50*'#')
    print(sorted_arges)
