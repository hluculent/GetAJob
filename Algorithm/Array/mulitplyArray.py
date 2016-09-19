# -*- coding:utf-8 -*-
import copy
"""
构建乘积数组
v给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
"""
class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return []
        n = len(A)
        B = [0]*n
        for i in range(n):
            tmp = copy.copy(A)
            tmp.remove(A[i])
            B[i] = reduce(lambda x,y: x*y,tmp)
        return B
