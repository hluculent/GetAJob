# -*- coding: utf-8 -*-

"""
（1）二叉树是有序树，即使只有一个子树，也必须区分左、右子树；

（2）二叉树的每个结点的度不能大于2，只能取0、1、2三者之一；

（3）二叉树中所有结点的形态有5种
"""
class TreeNode(object):
    def __init__(self, data, left, right):
        self.data = data
        self.right = right
        self.left = left

class BTree(object):
    def __init__(self, root=0):
        self.root = root