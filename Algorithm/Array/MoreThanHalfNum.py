# -*- coding:utf-8 -*-
"""
数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        table = {}
        numbers = list(numbers)
        for ele in numbers:
            if ele not in table:
                table[ele] = 1
            else:
                table[ele] += 1
        print table
        for key in table:
            if table[key] > len(numbers)/2:
                return key
        return 0

ans = Solution()
numbers = [1,2,3,2,2,2,5,4,2]
print ans.MoreThanHalfNum_Solution(numbers)


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        if not numbers:
            return 0
        numbers.sort()
        mid = numbers[len(numbers)/2-1]
        if numbers.count(mid) > len(numbers)/2:
            return mid
        else:
            return 0