# -*- coding: UTF-8 -*-

"""
1. LIFO
2. 栈顶---> ][][][]栈底
3. ADT
  Stack() 创建栈顶
  push(item) 向栈顶插入项
  pop() 返回栈顶的项，并从堆栈中删除该项
  clear() 清空堆栈
  empty() 判断堆栈是否为空
  size() 返回堆栈中项的个数
  *top() 返回栈顶的项
4.应用
    进制转换
"""

# vesion 1
class Stack1:
    def __init__(self):
        self.items = [] # 用列表表示

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def clear(self):
        del self.items[:]

    def empty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[self.size()-1]

# version 2
class Stack2:
    def __init__(self,size=16):# 设定默认空间
        self.stack = []
        self.size = size
        self.top = -1 #设定栈顶指针

    def setSize(self,size):
        self.size = size

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top + 1 == self.size:
            return True
        else:
            return False

    def top(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            return self.stack[self.top]

    def push(self, obj):
        if self.isFull():
            raise Exception("Stack Overflow")
        else:
            self.stack.append(obj)
            self.top += 1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            self.top -= 1
            return self.stack.pop()

    def show(self):
        print self.stack

    # 我自己加的哦
    def printsize(self):
        # return len(self.stack)
        return self.top + 1

# 应用篇1：进制转换
# 十进制转二进制：除以2求余后逆序输出
def divideBy2(decNumber):
    remstack = Stack2()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        # print 'show stack:',remstack.show()
        decNumber = decNumber // 2
        # print decNumber

    binString = ""
    while not remstack.isEmpty():
        binString += str(remstack.pop())
        # print 'now:',binString

    return binString

def example():
    stack1 = Stack2()
    print stack1.size # 我当成函数调用不成功,因为函数和变量同名了，先调用变量 >>> 16
    print stack1.printsize() # 这才是正确答案！>>> 0
    stack1.push('hi')
    stack1.push('you')
    stack1.show()
    print stack1.isEmpty()
    stack1.pop()
    stack1.show()
    # stack1.push(i for i in 'abcdefghijklmnopqrstuvwxyz')
    for i in 'abcdefghijklmnopqrstuvwxyz':
        try:
            stack1.push(i)
        except Exception:
            break
    stack1.show()
    print stack1.isFull()

if __name__ == '__main__':
    # print divideBy2(42)
    example()