# -*- coding:utf-8 -*_
"""
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        # 真想用函数解决问题,说是复杂度过大
        # return min(rotateArray)
        # 用二分吧
        """
        length = len(rotateArray)
        index = length / 2
        init = rotateArray[0]
        while init < rotateArray[index]:
            index = (length + index) / 2
        while rotateArray[index - 1] < rotateArray[index]:
            index -= 1
        return rotateArray[index]
        """
        # 直接线性比较
        init = rotateArray[0]
        for item in rotateArray:
            if item < init:
                return item
        return init