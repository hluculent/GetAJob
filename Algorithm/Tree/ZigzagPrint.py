# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution1:
    def Print(self, pRoot):
        if not pRoot:
            return []
        ans = [pRoot.val]
        nodeStore = [pRoot]
        tmp = []
        flag = True # 0 for ->; 1 for <-
        while nodeStore:
            if flag:
                for node in nodeStore:
                    if node.right:
                        ans.append(node.right.val)
                        tmp.append(node.right)
                    if node.left:
                        ans.append(node.left.val)
                        tmp.append(node.left)
                flag = False
                nodeStore = tmp.reverse()
            if not flag:
                for node in nodeStore:
                    if node.left:
                        ans.append(node.left.val)
                        tmp.append(node.left)
                    if node.right:
                        ans.append(node.right.val)
                        tmp.append(node.right)
                flag = True
                nodeStore = tmp.reverse()
        return ans

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        result = []
        nodes = [pRoot]
        flag = True
        while nodes:
            currentStack = []
            nextStack = []
            if flag:
                for node in nodes:
                    currentStack.append(node.val)
                    if node.left:
                        nextStack.append(node.left)
                    if node.right:
                        nextStack.append(node.right)
                nextStack.reverse()
                flag = False
            else:
                for node in nodes:
                    currentStack.append(node.val)
                    if node.right:
                        nextStack.append(node.right)
                    if node.left:
                        nextStack.append(node.left)
                nextStack.reverse()
                flag = True
            result.append(currentStack)
            nodes = nextStack
        return result

