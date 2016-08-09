# -*- coding: UTF-8 -*-

"""
1. FIFO
2. 队尾---> ][][][][ --->队头
3. ADT
    Queue() 创建队列
    enqueue(item) 向队尾插入项
    dequeue() 返回队首的项，并从队列中删除
    empty() 判断队列是否为空
    size()　返回队列中项的个数
4.应用
    约瑟夫斯问题(循环队列)
"""

# vesion1
class Queue1():
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) # 注意pop(0)是list中第一个元素，也就是最早进入的元素
                                # 也就是队头元素

    def empty(self):
        return self.size() == 0 # 好明快

    def size(self):
        return len(self.items)

    # 我自己加的，显示队列中所有元素
    # 按照 队头 到 队尾 的顺序
    def show(self):
        print self.items

# version 2
class Queue2():
    def __init__(self,size=16):
        self.size = size
        self.front = -1
        self.rear = -1
        self.queue = []

    def enqueue(self, item):
        if self.isfull():
            raise Exception("queue is full")
        else:
            self.queue.append(item)
            self.rear += 1

    def dequeue(self):
        if self.isempty():
            raise Exception("queue is empty")
        else:
            self.front += 1 # 开始是-1，要先加一再返回下标所在的值
            return self.queue[self.front]

    def isfull(self):
        return self.rear - self.front + 1 == self.size

    def isempty(self):
        return self.front == self.rear



# 应用篇1
def josephus(namelist, num):
    simqueue = Queue1()
    for name in namelist:
        simqueue.enqueue(name)
    simqueue.show()
    while simqueue.size() > 1:
        for i in xrange(num):
            simqueue.enqueue(simqueue.dequeue())
            simqueue.show()
        simqueue.dequeue()
    return simqueue.dequeue()

if __name__ == "__main__":
    print josephus(['Bill','David','Kent','Susan','Brad'],3)
