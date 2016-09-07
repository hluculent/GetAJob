# -*-coding:utf-8 -*-

"""
（有序区，无序区）。
在无序区里找一个最小的元素跟在有序区的后面。对数组：比较得多，换得少。
! best case: still O(N^2)
对数组是不稳定的，对链表是稳定的
"""
def selectionSort(L):
    N = len(L)
    for i in range(N-1):
        min_index = i
        for j in range(i+1, N):
            if L[min_index] > L[j]:
                min_index = j
        if min_index != i:
            L[min_index], L[i] = L[i], L[min_index ]