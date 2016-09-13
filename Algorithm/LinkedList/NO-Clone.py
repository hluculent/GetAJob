# -*- coding:utf-8 -*-

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # # 还是不知道为什么这样就返回空
        # if not pHead or not pHead.next:
        #     return pHead
        # while pHead.next:
        #     cp_Head = pHead
        #     cp_Head.label = pHead.label
        #     cp_Head.next = pHead.next
        #     cp_Head.random = pHead.random
        #     pHead = pHead.next
        #     cp_Head = cp_Head.next
        # return cp_Head
        mem=dict()
        for i,n in enumerate(iter_node(pHead)):
            mem[id(n)]=i # 为节点的顺序存一个地址
        lst=[RandomListNode(n.label) for n in iter_node(pHead)]
        for t,f in zip(iter_node(pHead),lst):
            if t.next:
                f.next=lst[mem[id(t.next)]]
            if t.random:
                f.random=lst[mem[id(t.random)]]
        return lst[0] if lst else None

def iter_node(root):
    while root:
        yield root
        root=root.next

