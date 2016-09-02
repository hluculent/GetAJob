# -*- coding:utf-8 -*-
"""
跳台阶
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""
# 这种做法会有越界错误
# class Solution:
#     def jumpFloor(self, number):
#         # write code here
#         # x个1， y个2， x+2y=n
#         # 对于每个可行解，求一次组合 C(x, x+y)
#         # 求和
#         if not number:
#             return 0
#         count = 0
#         for one in range(number + 1):
#             if not (number - one) % 2: # 有偶数个台阶
#                 two = (number - one) / 2
#                 # one + two个数，抽出two C(one+two, one)
#                 count += Solution.fac(one+two) / (Solution.fac(one) * Solution.fac(two))
#         return count
#
#     def fac(self, n):
#         if n == 0:
#             return 1
#  		return reduce(lambda x, y:x * y, range(1, n + 1))

class Solution:

    def jumpFloor(self, number):
        # write code here
        # 想象成递归问题: 斐波那契数列 in specific
        # 然后用迭代
        if number == 0:
            return 0
        a = 1
        b = 1
        for i in range(number):
            a, b = b, a+b
        return a

