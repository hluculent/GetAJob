# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        ans = [[pRoot.val]]
        nodeStore = [pRoot]
        while nodeStore: # 因为要分成打印，每次还是要清空比较好
            tmpans = []
            tmpnode = []
            for node in nodeStore:
                if node.left:
                    tmpans.append(node.left.val)
                    tmpnode.append(node.left)
                if node.right:
                    tmpans.append(node.right.val)
                    tmpnode.append(node.right)
            if tmpans:ans.append(tmpans)
            nodeStore = tmpnode
        return ans
