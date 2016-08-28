# -*- coding:utf-8 -*-

"""
题目描述

在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
class Solution:
    # array 二维列表
    def Find(self, array, target):
        # write code here
        m = len(array)  # rows
        n = len(array[0])  # columns
        if m == 0 or n == 0:
            return 0
        # if target > array[m-1][n-1]:
        #     return 0
		# 从右上角开始
        row = 0
        col = n-1
        while row < m and col >= 0:  # 下标从0开始
            if array[row][col] == target:
                return 1
            elif array[row][col] > target:
                col -= 1
            elif array[row][col] < target:
                row += 1
        return 0