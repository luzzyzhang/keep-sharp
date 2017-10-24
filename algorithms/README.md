
# 常用算法总结

## 排序
1. [快速排序](qsort.py)
2. [归并排序](merge_sort.py)
3. [堆排序](heap_sort.py)
4. [冒泡排序](bubble_sort.py)
5. [插入排序](insert_sort.py)
6. [选择排序](select_sort.py)
7. [希尔排序](shell_sort.py)

|名称|稳定性|平均时间复杂度|最坏时间复杂度|空间复杂度|
|---|---|---|---|---|
|快速排序|X|O(nlogn)|O(n^2)|O(logn),O(n)|
|归并排序|√|O(nlogn)|O(nlogn)|O(n)|
|堆排序|X|O(nlogn)|O(nlogn)|O(1)|
|冒泡排序|√|O(n^2)|O(n^2)|O(1)|
|选择排序|X|O(n^2)|O(n^2)|O(1)|
|插入排序|√|O(n^2)|O(n^2)|O(1)|
|希尔排序|X|O(nlog^2n)|O(n^2)|O(1)|

## 查找
1. [二分查找](traverse_binary_tree.py)
