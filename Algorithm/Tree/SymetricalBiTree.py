# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        return self.compare(pRoot.left, pRoot.right)

    def compare(self, rt1, rt2):
        if not rt1 and not rt2:
            return True
        if not (rt1 and rt2) or rt1.val != rt2.val:
            return False
        return self.compare(rt1.left, rt2.right) and self.compare(rt1.right, rt2.left)