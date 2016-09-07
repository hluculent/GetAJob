# -*- coding:utf-8 -*-

"""
希尔排序是缩减增量的插入排序
不稳定
最好O(NlogN），最坏O（N^2)
"""
def shellSort(L):
    N = len(L)
    gap = N >> 1  # N/2
    while gap > 0:
        for pos in range(gap, N):
            tmp = L[pos]
            pre_pos = pos - gap
            while pre_pos >= 0 and L[pre_pos] > tmp:
                L[pre_pos + gap] = L[pre_pos]
                pre_pos -= gap
            L[pre_pos + gap] = tmp
        gap >>= 1