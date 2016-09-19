# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s or len(s)==1:
            return s
        length = len(s)
        k = n%length
        return s[k:]+s[:k]
        