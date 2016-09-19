# -*- coding:utf-8 -*-
"""
数组中只出现一次的数字
一个整型数组里除了两个数字之外，其他的数字都出现了两次。
请写程序找出这两个只出现一次的数字。
"""
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        ans = []
        for ele in array:
            if array.count(ele)==1:
                ans.append(ele)
            if len(ans)==2:
                break

        return ans

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        can = []
        for ele in array:
            if ele not in can:
                can.append(ele)
            else:
                can.remove(ele)

        return can