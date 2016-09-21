# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        if pHead.val == pHead.next.val:
            pnode = pHead.next.next
            while pnode and pnode.val==pHead.val:
                pnode = pnode.next
            return self.deleteDuplication(pnode)
        else:
            pHead.next = self.deleteDuplication(pHead.next)
            return pHead