# -*- coding:utf-8 -*-
"""
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # 能连成路径的只有 父节点和某子节点
        # 路径一定要从根节点开始， 到叶子节点结束
        if not root or root.val > expectNumber:
            return []
        if root and not root.left and not root.right and \
                        root.val == expectNumber: # 只有叶子结点才返回
            return [[root.val]] # 返回的列表是节点的值这点太不可思议了
        ans = []
        left = self.FindPath(root.left, expectNumber - root.val)
        right = self.FindPath(root.right, expectNumber - root.val)
        for ele in left+right:
            ans.append([root.val]+ele)
        return ans

