# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        array = [1]
        Q2 = Q3 = Q5 = []
        while len(array) < index:
            last = array[-1]
            Q2.append(last*2)
            Q3.append(last*3)
            Q5.append(last*5)
            cur = min(Q2+Q3+Q5)
            if cur in Q2:
                Q2.remove(cur)
            if cur in Q3:
                Q3.remove(cur)
            if cur in Q5:
                Q5.remove(cur)
            array.append(cur)
        return array[-1]

# -*- coding:utf-8 -*-
class Solution1:
    def GetUglyNumber_Solution(self, index):
        if index < 1:
            return 0
        res = [1]
        t2 = t3 = t5 = 0
        nextIdx = 1
        while nextIdx < index:
            minNum = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
            res.append(minNum)
            while res[t2] * 2 <= minNum:
                t2 += 1
            while res[t3] * 3 <= minNum:
                t3 += 1
            while res[t5] * 5 <= minNum:
                t5 += 1
            nextIdx += 1
        return res[nextIdx - 1]
