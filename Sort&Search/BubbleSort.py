# -*- coding: utf-8 -*-

"""
（无序区，有序区），从无序区通过交换找到最大元素放到有序区前端
O(N^2), STABLE
! best case: still O(N^2)
"""
def bubbleSort(L):
    for i in range(len(L)-1, 0, -1):
        for j in range(0, i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]