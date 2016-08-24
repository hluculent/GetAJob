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
class Node1(): # 定义节点类
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
        self.head = Node1(None)
        # self.head.setNext(None)  # 没意义，表头默认指针域为空

    def add(self, item): # 只能在表头添加元素太蠢了
        tmp = Node1(item)
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

# version 2
# class Node(object):
class Node():
    def __init__(self, item):  # 创建一个节点类，要用值去创建
        self._data = item
        self._next = None
        # self._header = header #注意分清楚，node只是一个节点类，没有表头

    def getData(self):
        return self._data

    def getNext(self):
        return self._next

    def setData(self, item):
        self._data = item

    def setNext(self, item):
        self._next = item

class LinkedList():
    def __init__(self):
        self._head = None  # 本来想要创建一个头节点的，然后关系混乱了
        self._size = 0
        # self._tail = None

    def isEmpty(self):
        return self._head == None

    def append(self, item): # 在表尾增加元素
        tmp = Node(item)
        if self.isEmpty(): # 如果还没插入值，要将表头的None值改掉
            self._head = tmp  # 所谓的head、Next都应该是节点类型，而不是值类型
        else:
            cur = self._head
            while cur.getNext() != None:
                cur = cur.getNext()
            tmp.setNext(tmp)
        # tmp.setNext(self._tail.getNext)
        # self._tail = tmp  # tail应该是一个下标指示比较好吧
        self._size += 1

    def insert(self, pos, item): # 在某个位置插入元素
        if pos > self._size or pos < 0:
            raise Exception("Index out of range")
        else:
            tmp = Node(item)
            count = 1
            cur = self._head # 又要开始遍历了
            # pre = None # 按照位置遍历，要记录前一个节点，要处理它的指针
            while count < pos-1:
                cur = cur.getNext()
                count += 1
            tmp.setNext(cur.getNext())
            cur.setNext(tmp)
            self._size += 1

    def remove(self, pos):
        if pos < 0 or pos > self._size:
            raise Exception("There is no data here")
        else:
            count = 1
            cur = self._head
            while count < pos-1:
                cur = cur.getNext()
                count += 1
            # 到达指定地点
            cur.setNext(cur.getNext().getNext())
            self._size -= 1

    def search(self, item):
        cur = self._head
        while cur.getNext() != None:
            if cur.getData() == item:
                return True
            cur = cur.getNext()
        return False

    def travel(self):
        cur = self._head
        print 'Show linked list:'
        while cur != None:
            print cur.getData(),
            cur = cur.getNext()
        print '\n'

if __name__=='__main__':
    a=LinkedList()
    for i in range(1,10):
        a.append(i)
    print a._size
    a.travel()
    print a.search(6)
    # print a.index(5)
    a.remove(4)
    a.travel()
    a.insert(4,100)
    a.travel()