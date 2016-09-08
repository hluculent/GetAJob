# -*- coding:utf-8 -*-
"""
合并两个排序的链表
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
"""
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        elif not pHead2:
            return pHead1
        else:
            if pHead1.val < pHead2.val:
                pHead = pHead1
                pHead.next = self.Merge(pHead1.next, pHead2)
            else:
                pHead = pHead2
                pHead.next = self.Merge(pHead1, pHead2.next)
        return pHead
