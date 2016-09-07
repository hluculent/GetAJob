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
        print [x for x in arr[1:] if x < pivot] + \
               [pivot] + \
               [x for x in arr[1:] if x >= pivot]

# version 3 easy and standard
def part(L, low, high):
    pivot = L[low]
    while low < high:
        while low < high and L[high] >= pivot:
            high -= 1
        L[low] = L[high]
        while low < high and L[low] < pivot:
            low += 1
        L[high] = L[low]
    L[low] = pivot
    return low

def Qsort(L, low, high):
    if low < high:
        pivot_pos = part(L, low, high)
        # print L[pivot_pos]
        Qsort(L, low, pivot_pos)
        Qsort(L, pivot_pos+1, high)


# quickSort([19,15,12,18,21,36,45,10],0,8)
# print qsort([19,15,12,18,21,36,45,10])
L = [19,15,12,18,21,36,45,10]
Qsort(L,0,7)
print L