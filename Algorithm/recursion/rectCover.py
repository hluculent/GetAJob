# -*- coding:utf-8 -*-
"""
矩形覆盖
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""
class Solution:
    def rectCover(self, number):
        # write code here
        # 因为大矩形宽度只有2，所以不存在交叉覆盖的状况
        # f(1) = 1
        # f(2) = 2
        # f(3) = 3
        # f(4) = 5 ! 偶数会增加一个横着的对
        # f(5) = 8
        # 这样想太复杂了，跟跳台阶联系起来
        # 如果左上放的是竖的，下面还有f(n-1)种
        # 如果左上放的是横的，下面是f(n-2)种
        if number < 1:
            return 0
        a = 1
        b = 1
        for _ in range(number):
            a, b = b, a+b
        return a