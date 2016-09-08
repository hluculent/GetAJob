# -*- coding:utf-8 -*-

"""
基数排序
补零，一个个比
稳定，可用桶排序实现
桶排序：将值为i的元素放入i号桶，最后依次把桶里的元素倒出来。
k代表数值中的"数位"个数
n代表数据规模
m代表数据的最大值减最小值
基数 平均 O（k*n), worst O（n^2)
桶 O（n) 空间O（m）
"""

def radixSort(nums):
    max_num = max(nums)  # 求最值的函数算法复杂度O(n)
    bucket = [[] for _ in range(10)]
    exp = 1
    while max_num / exp > 0:
        for num in nums:
            bucket[(num / exp) % 10].append(num)
        nums = []
        for each in bucket:
            nums.extend(each)
        bucket = [[] for _ in range(10)]
        exp *= 10