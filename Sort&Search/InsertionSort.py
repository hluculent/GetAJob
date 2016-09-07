# -*- coding: utf-8 -*-

"""
（有序区，无序区）。
把无序区的第一个元素插入到有序区的合适的位置。对数组：比较得少，换得多。
O(N^2), STABLE
! best case: still O(N^2)
"""


def insertionSort(L):
    for i in range(1, len(L)):
        tmp = L[i]
        j = i -1
        while j >= 0 and tmp < L[j]:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = tmp

