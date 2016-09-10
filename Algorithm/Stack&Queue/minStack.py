# -*- coding:utf-8 -*-
"""
包含min函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
"""

class Solution:
    #stack = []
    # 其实不能这么写，因为stack只可以看到头顶的元素
    # 应该在push之前就确认好最小的元素放在里边
    # pop的时候也要注意是不是pop出去了
    # 更重要的是，对于新建的类/数据结构，要记得在引用变量前加self
    def __init__(self):
        self.stack = []
    def push(self, node):
        self.stack.append(node)
    def pop(self):
        return self.stack.pop()
    def top(self):
        print self.stack.pop()
    def min(self):
        return min(self.stack)