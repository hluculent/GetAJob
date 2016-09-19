# -*- coding:utf-8 -*-
"""
wrong anwser
"""
import copy
class Solution:
    def InversePairs(self, A):
        # 纯找规律
        # A.sort() vs A
        # index x,y: y>x, (y<x), y=x看位置，靠前看A前有多少大于它，靠后看A.sort()它后面还有多少个
        B = copy.deepcopy(A)
        A.sort()
        count = 0
        for x in range(len(A)):
            y = B.index(A[x])
            if y > x:
                count += y-x
            elif x == y:
                if x < len(A)/2:
                    for ele_b in B[:y]:
                        if ele_b > B[y]:
                            count += 1
                if x > len(A)/2:
                    count += len(A) - x - 1
        return count

ans = Solution()
A1 = [1,2,3,4,5,6,7,0]
A2 = [1,3,2,0,5,7,6,4]
A3 = [6,4,7,2,5,3,0,1]
print ans.InversePairs(A3)