# -*- coding:utf-8 -*-
"""
调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。

"""
class Solution:
    def reOrderArray(self, array):
        # write code here
        # 相对位置不变，就不能使用两头换的方法了
        odd = []
        even = []
        for num in array:
            if num%2:
                odd.append(num)
            else:
                even.append(num)
        odd.extend(even)
        # 注意不能直接return extend的表达式，会返回None
        return odd