# -*- coding: utf-8 -*-
"""可以使用内置 heapq 实现
   https://docs.python.org/3/library/heapq.html#basic-examples
def heapsort(iterable):
...     h = []
...     for value in iterable:
...         heappush(h, value)
...     return [heappop(h) for i in range(len(h))]
...
>>> heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

def heap_sort(lst):
    build_heap(lst)
    print(lst)
    print(50*'-')
    for x in range(len(lst)-1, 0, -1):
        lst[0], lst[x] = lst[x], lst[0]
        heapify(lst, 0, x)
        print(lst)
    print(50*'~')
    return lst


def build_heap(lst):
    n = len(lst) - 1
    for i in range(n//2, -1, -1):
        heapify(lst, i, n)


def heapify(lst, i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if (left < n and lst[left] > lst[largest]):
        largest = left
    if (right < n and lst[right] > lst[largest]):
        largest = right

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, largest, n)


if __name__ == '__main__':
    # lst = [32, 46, 77, 4344564, 7322, 3, 46, 7, 32457, 7542, 4, 667, 54]
    lst = [6, 1, 3, 10, 5, 4, 8, 7, 9, 2]
    # lst = [2, 6, 3, 4, 5]
    heap_sort(lst)
    print(lst)
