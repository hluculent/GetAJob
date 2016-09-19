# -*- coding:utf-8 -*-
"""
和为S的连续正数序列
输出所有和为S的连续正数序列。
序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
"""
class Solution:
    def FindContinuousSequence(self, tsum):
        begin = 1
        end = 2
        total = 3
        ans = []
        mid = (1+tsum)>>1
        while begin < mid and end<tsum:
            if total == tsum:
                ans.append(range(begin,end+1))
                end += 1
                total += end
            if total<tsum:
                end+=1
                total += end
            if total>tsum:
                total -= begin
                begin+=1
        return ans