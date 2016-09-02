# -*- coding:utf-8 -*-

"""
变态跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""
class Solution:
    def jumpFloorII(self, number):
        # write code here
        # 自己写出前几个台阶
        # f(1) = 1
        # f(2) = f(1) + 1
        # f(3) = f(2) + f(1) + 1
        # 需要把每个f(i)记录下来
        if number <= 0:
            return 0
        a = 1
        f = []
        for _ in range(1, number): # range(4) = [0, 1, 2, 3]
            f.append(a)
            #a = reduce(lambda x, y: x + y + 1, f)
            a = sum(f) + 1
        return a