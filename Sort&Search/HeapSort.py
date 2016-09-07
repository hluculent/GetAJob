# -*- coding: utf-8 -*-

"""
完全二叉树，数组,
不稳定
（最大堆，有序区）。
从堆顶把根卸出来放在有序区之前，再恢复堆
"""
"""
最大堆为例子，插入 O(logN), 查找 O(1), 删除 O(logN) 调整
某节点 i， 父节点为 i/2， 左儿子 i*2, 右儿子 i*2 + 1
"""
def heapAdjust(L, i, size):
    parent = i
    while True:
        child = 2 * parent + 1
        if child >= size:
            break
        # 为什么是加1？？？
        if child + 1 < size and L[child] < L[child + 1]:
            child += 1
        if L[parent] < L[child]:
            L[parent], L[child] = L[child], L[parent]
        else:
            break

def heapBuild(L, size):
    for i in range(size//2, -1, -1):
        heapAdjust(L, i, size)

def heapSort(L):
    size = len(L)
    heapBuild(L, size)
    print "Big", L
    for i in range(size-1, 0, -1):
        L[i], L[0] = L[0], L[i]
        heapAdjust(L, 0, i)