# -*- coding:utf-8 -*-
"""
输入一个链表，从尾到头打印链表每个节点的值。
输入描述:
输入为链表的表头


输出描述:
输出为需要打印的“新链表”的表头
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode == None:
            return []
        #print ''.join(x for x in self[::-1])
        ans = []
        while listNode.next:
            ans.append(listNode.val)
            listNode = listNode.next
        ans.append(listNode.val)
        # 有没有更简洁的循环赋值方法?
        return ans[::-1]