# -*- coding:utf-8 -*-
"""
二叉树的下一个结点
"""
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return
        if pNode.right:
            pNode=pNode.right
            while pNode.left:
                pNode=pNode.left
            return pNode
        else:
            while pNode.next:
                if pNode==pNode.next.left:
                    return pNode.next
                else:
                    pNode=pNode.next
        return
