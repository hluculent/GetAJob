# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead or not pHead.next:
            return
        pHead1 = pHead.next
        pHead2 = pHead.next.next
        while pHead1.val != pHead2.val:
            pHead1 = pHead1.next
            pHead2 = pHead2.next.next
        pHead2 = pHead
        while pHead1.val != pHead2.val:
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return pHead1