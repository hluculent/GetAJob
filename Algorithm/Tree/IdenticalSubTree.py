#-*- coding:utf-8 -*-
"""
输入两棵二叉树A，B，判断B是不是A的子结构。
（ps：我们约定空树不是任意一个树的子结构）
"""
#class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # 如果值相等，则往下比较
        # 如果值不等，则继续判断是否有根节点值相等
        # 递归
        flag = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                flag = self.searchDown(pRoot1, pRoot2)
            # else:
            if not flag:
                flag = self.HasSubtree(pRoot1.left, pRoot2) or \
                self.HasSubtree(pRoot1.right, pRoot2)
        return flag

    def searchDown(self, pRoot1, pRoot2):
        if not pRoot2: # 树B已经搜索完毕
            return True
        if not pRoot1 or pRoot1.val != pRoot2.val:
            return False
        # 递归
        return self.searchDown(pRoot1.left, pRoot2.left) and \
                self.searchDown(pRoot1.right, pRoot2.right)
