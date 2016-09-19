# -*- coding:utf-8 -*-
"""
在一个字符串(1<=字符串长度<=10000，全部由大小写字母组成)
中找到第一个只出现一次的字符,并返回它的位置
"""
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        ans = []
        store = []
        for ele in s:
            if ele in ans:
                ans.remove(ele)
                store.append(ele)
            elif ele not in ans and ele not in store:
                ans.append(ele)

        return s.index(ans[0])

# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        for ele in s:
            if s.count(ele) == 1:
                return s.index(ele)
        return -1