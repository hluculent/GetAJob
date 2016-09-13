# -*- coding:utf-8 -*-
"""
二叉搜索树与双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
	def Convert(self, pRootOfTree):
		# 双向链表其实还是树的结构
		# 左叶子就是左节点，右儿子就是右节点
		# 二叉搜索树 左<中<右； 排序的双向链表 左<中<右
		# 左子树递归变成一个链表
		if not pRootOfTree or (not pRootOfTree.left and not pRootOfTree.right):
			return pRootOfTree
		# left
		self.Convert(pRootOfTree.left)
		if pRootOfTree.left:
			if pRootOfTree.left.right:
				pRootOfTree.left = pRootOfTree.left.right
			pRootOfTree.left.right = pRootOfTree
		# right
		self.Convert(pRootOfTree.right)
		if pRootOfTree.right:
			if pRootOfTree.right.left:
				pRootOfTree.right = pRootOfTree.right.left
			pRootOfTree.right.left = pRootOfTree

		while pRootOfTree.left:
			pRootOfTree = pRootOfTree.left

		return pRootOfTree