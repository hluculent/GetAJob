# -*- coding:utf-8 -*-
"""
输入一个链表，反转链表后，输出链表的所有元素
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        #ls = []
        #while pHead.next:
        #    ls.append(pHead.val)
        #    pHead = pHead.next
        #ls.append(pHead.val)
        #return ls[::-1]
        """
        结果要返回节点，而不是节点的值
        """
        if not pHead or not pHead.next:
            return pHead # 如果pHead是空节点，也会返回None，如果下一个为空，返回pHead

        last = None
        # before last(None) -> pHead -> tmp
        # after None <- last <- pHead <- tmp

        while pHead:
            tmp = pHead.next
            pHead.next = last
            last = pHead
            pHead = tmp

        return last