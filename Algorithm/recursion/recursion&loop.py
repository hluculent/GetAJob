# -*- coding:utf-8 -*-

"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
"""
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return 1
        # return Solution.Fibonacci(n-1) + Solution.Fibonacci(n-2)
        # unbound method Fibonacci() must be called with Solution instance as first argument (got int instance instead)

        # turn Solution.Fibonacci(self,n-1) + Solution.Fibonacci(self, n-2)
        # 超时:您的程序未能在规定时间内运行结束，请检查是否循环有错或算法复杂度过大。

        # 用一个列表储存已经计算过的值
        #f = [0,1,1] + [0] * 37 # len(f) = 40
        f = [0,1,1]
        for i in range(3, n+1):
            #f[i] = f[i-2] + f[i-1]
            f.append(f[i-2] + f[i-1])

        return f[n]
