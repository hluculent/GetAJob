# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    index=-1
    def Serialize(self, root):
        if not root:
            return '#'
        # 不间隔的话就分不清值在个位数以上的节点了
        return str(root.val)+','+self.Serialize(root.left)+','+self.Serialize(root.right)

    def Deserialize(self, s):
        return self.De(s.split(','),self.index)
    def De(self,sls,index):
        self.index+=1
        if self.index>=len(sls):
            return None
        root=None
        if sls[self.index]!='#':
            root=TreeNode(int(sls[self.index]))
            root.left=self.De(sls,self.index)
            root.right=self.De(sls,self.index)
        return root