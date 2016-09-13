# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # 二叉搜索树 左边小，右边大
        # 后序遍历：左边-->右边-->根
        if not sequence or len(sequence) == 0:
            return False
        length = len(sequence)
        root = sequence[-1]
        index = 0
        while sequence[index] < root:
            index += 1
        #left_flag, right_flag = True, True
        for i in range(index):
            if sequence[i] > root:
                #left_flag = False
                #return left_flag
                return False
        for j in range(index, length-1):
            if sequence[j] < root:
                #right_flag = False
                #return right_flag
                return False
        self.VerifySquenceOfBST(sequence[:index])
        self.VerifySquenceOfBST(sequence[index:length-1])
        return True

# test case
s = [4,8,6,12,16,14,10]

if __name__ == '__main__':
    instance = Solution()
    ans = instance.VerifySquenceOfBST(sequence=s)
    if ans == True:
        print 'test ok'