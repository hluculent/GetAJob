# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        front = 0
        back = len(array)-1
        while array[front] < array[back]:
            if array[front] + array[back] == tsum:
                return [array[front],array[back]]
            if array[front] + array[back] < tsum:
                front += 1
            if array[front] + array[back] > tsum:
                back -= 1
        return []
