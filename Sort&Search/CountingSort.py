# -*- coding: utf-8 -*-
"""
计数排序
稳定
统计小于等于该元素值的元素的个数i，于是该元素就放在目标数组的索引i位（i≥0）。
O（n+m)的时间空间复杂度
"""
def countSort(L):
    max_num = max(L)
    cnt_array = [0] * max_num
    for n in L:
        cnt_array[n] += 1
    ans = []
    for i in range(max_num):
        ans.extend([i]*cnt_array[i])
    return ans