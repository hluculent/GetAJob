# -*- coding: UTF-8 -*-

"""
1. 单向链表、单向循环链表、双向链表、双向循环链表
2. ADT
    SinLinkedlist() 创建单向链表
    add(item) 插入数据项
    remove(item) 删除数据项
    search(item) 在链表中查找数据项是否存在
    empty() 判断链表是否为空
    size() 返回链表中数据项的个数
**数组是连续列表，链表是链接列表，二者在概念和结构上完全不同，因此list不能用于实现链表。
**在Python中，则可以采用“引用+类”来实现链表。

"""

# version 1
class Node: # 定义节点类
    def __init__(self, initdata):
        self._data = initdata  # 信息域
        self._next = None  # 指针域

    def getData(self):
        return self._data

    def getNext(self):
        return self._next

    def setData(self, newdata):
        self._data = newdata

    def setNext(self, newnext):
        self._next = newnext

class SinLinkedlist: # 不能写成SinLinkedlist(Node)，因为不是类继承，是变量作为实例继承
    def __init__(self):
        self.head = Node(None)
        self.head.setNext(None)

    def add(self, item):
        tmp = Node(item)
        tmp.setNext(self.head.getNext)
        self.head.setNext(tmp)

    def remove(self, item):
        prev = self.head
        while prev.getNext() != item:
            cur = prev.getNext()
            if cur.getData() == item:
                prev.setNext(cur.getNext())
            prev = prev.getNext()

    def search(self, item):
        cur = self.head.getNext()
        while cur!= self.head:
            if cur.getData() == item:
                return True
            cur = cur.getNext()

        return False

    def empty(self):
        return  self.head.getNext() == self.head

    def size(self):
        count = 0
        cur = self.head.getNext()
        while cur != self.head:
            count += 1
            cur = cur.getNext()

        return count

