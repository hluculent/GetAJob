# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
## 这种做法不可以，说是在非序列类型中迭代
# class Solution:
#     def TreeDepth(self, pRoot):
#         # BFS
#         if not pRoot:
#             return -1
#         depth = 0
#         curNode = pRoot
#         candidateNode = []
#         # 每次扩展一层，放在一个列表里边，拓展的节点放到另一个列表里边
#         while depth == 0 or candidateNode:
#             for node in curNode:
#                 if node.left:
#                     candidateNode.append(node)
#                 if node.right:
#                     candidateNode.append(node)
#                 depth += 1
#                 curNode = []
#                 curNode.extend(candidateNode)
#                 candidateNode = []
#         return depth

class Solution:
    def TreeDepth(self, pRoot):
        # BFS
        if not pRoot:
            return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))+1