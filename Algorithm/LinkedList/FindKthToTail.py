# -*- coding:utf-8 -*-
"""
链表中倒数第k个结点
"""

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

	def FindKthToTail(self, head, k):
		# 隔着k的两个变量一起走，一个走到头，另一个就是倒数第k个
		# 注意边界条件：没有k的长度
		if not head or k < 1:
			return
		front, back, flag = head, head, 1
		# 头节点算第一个节点
		while front.next:
			if flag == k:
				break
			front = front.next
			flag += 1
		if flag < k:
			return
		while front.next:
			front = front.next
			back = back.next
		return back