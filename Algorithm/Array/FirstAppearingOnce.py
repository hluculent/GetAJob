# -*- coding:utf-8 -*-
class Solution:
    s = ''

    def FirstAppearingOnce(self):
        # for ele in set(self.s):   # set会改变顺序
        for ele in self.s:
            if self.s.count(ele)==1:
                return ele
        return '#'

    def Insert(self, char):
        self.s += char