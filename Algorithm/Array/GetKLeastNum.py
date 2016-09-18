# -*- coding:utf-8 -*-
"""
最小的K个数
输入n个整数，找出其中最小的K个数。
例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4
"""

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or k<0 or k>len(tinput):
            return [] # return 0 不行
        tinput.sort()
        return tinput[:k]

ans = Solution()
intarr = [4,5,1,6,2,7,3,8]
print ans.GetLeastNumbers_Solution(intarr, 10)