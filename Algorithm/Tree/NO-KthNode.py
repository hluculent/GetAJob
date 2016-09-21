# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def inorder(pRoot):
    # 中序遍历，只需要找到第k个，不必全部遍历，考虑使用生成器延迟计算
    if pRoot:
        if pRoot.left:
            for lt in inorder(pRoot.left):
                yield lt
        yield pRoot
        if pRoot.right:
            for rt in inorder(pRoot.right):
                yield rt

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if k < 1 or not pRoot:
            return None
        for i, node in enumerate(inorder(pRoot)):
            if i==k-1:
                return node
        return None


class Solution1:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if pRoot==None or k<=0:
            return None
        p=pRoot
        i=0
        stack=[]
        while stack or p:
            while p:
                stack.append(p)
                p=p.left
            p=stack.pop()
            i+=1
            if i==k:
                return p
            p=p.right
        return None