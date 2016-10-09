# -*- coding:utf-8 -*-
"""
wrong anwser
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007 
输入描述:
题目保证输入的数组中没有的相同的数字
数据范围：
	对于%50的数据,size<=10^4
	对于%75的数据,size<=10^5
	对于%100的数据,size<=2*10^5
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
