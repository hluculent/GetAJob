# -*- coding:utf-8 -*-
"""
整数中1出现的次数（从1到n整数中1出现的次数）
"""
# class Solution:
#     def NumberOf1Between1AndN_Solution(self, n):
#         # write code here
#         if n <= 0:
#             return 0
#         count = 0
#         for ele in range(1,n+1):
#             while ele:
#                 if ele%10 == 1:
#                     count+= 1
#                 ele = ele/10
#         return count

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        ones, m = 0, 1
        while m <= n:
            ones += (n/m + 8) / 10 * m + (n/m % 10 == 1) * (n%m + 1)
            m *= 10
        return ones

ans = Solution()
print ans.NumberOf1Between1AndN_Solution(1047)