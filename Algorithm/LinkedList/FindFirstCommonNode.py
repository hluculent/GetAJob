# -*- coding:utf-8 -*-
"""
两个链表的第一个公共结点
输入两个链表，找出它们的第一个公共结点。
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        list1 = []
        if not pHead1 or not pHead2:
            return None
        while pHead1.next:
            list1.append(pHead1.val)
            pHead1 = pHead1.next
        list1.append(pHead1.val)

        while pHead2:
            if pHead2.val in list1:
                return pHead2
            pHead2 = pHead2.next

        return None