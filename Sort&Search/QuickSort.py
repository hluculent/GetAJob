# -*- coding: utf-8 -*-

"""
快排，分治法
（小数，基准元素，大数）。
在区间中随机挑选一个元素作基准，将小于基准的元素放在基准之前，
大于基准的元素放在基准之后，再分别对小数区与大数区进行排序。
不稳定，bestO(logN), worst O(N^2), avg O(NlogN)
"""
# version 1 I hate this, still can't understand it
def partition(L, begin, end):
    pivot = L[begin]
    pivot_index = begin
    print 'pivot:',pivot
    for i in range(begin+1, end):
        print 'i:',i
        if L[i] <= pivot:
            pivot_index += 1
            print 'pivot_index:',pivot_index
            if pivot_index != i:
                L[pivot_index], L[i] = L[i], L[pivot_index]
        print 'l1:',L
    L[begin], L[pivot_index] = L[pivot_index], L[begin]
    print 'L2:',L
    return pivot_index

def quickSort(L, begin, end):
    if begin >= end -1:
        return
    # 返回位置有什么意思呢？
    pivot_pos = partition(L, begin, end)
    quickSort(L, begin, pivot_pos)
    quickSort(L, pivot_pos+1, end)

# version 2 I like this
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort([x for x in arr[1:] if x < pivot]) + \
               [pivot] + \
               qsort([x for x in arr[1:] if x >= pivot])

quickSort([49,38,65,97,76,13,27],0,7)