# -*-coding:utf-8 -*-

"""
stable

"""
def mergeSort(L):
    if len(L) <= 1:
        return L

    mid = len(L) / 2
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result