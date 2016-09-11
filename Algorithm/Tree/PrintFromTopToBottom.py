# -*- coding:utf-8 -*-
"""
从上往下打印二叉树
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    #def __init__(self):
    #    self.ans = []
    #def PrintFromTopToBottom(self, root):
    #    self.ans.append(self.root.val)
    #    self.PrintFromTopToBottom(self.root.left)
    #    self.PrintFromTopToBottom(self.root.right)
    #	return ans
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        # 用一个等待队列存左右节点
        queue = []
        # 用一个列表存打印结果
        result = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result