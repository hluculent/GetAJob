# one line
str = raw_input()
print str

# multiple lines
import sys
for line in sys.stdin:
    for value in line.split():
        print(value)

# !/usr/bin/env python
# coding=utf-8
while 1:
	s = raw_input()
	if s != "":
		for x in s.split():
			a.append(int(x))

		print sum(a)
	else:
		break

trial = int(raw_input().strip())

def JumpStairs(k):
	m = k-1
	if m ==0 or m==1 or m==2:
		return m
	else:
		return JumpStairs(k-1) + JumpStairs(k-2)

ans = []
# while trial:
for i in range(trial):
	tmp = JumpStairs(int(raw_input().strip()))
	ans.append(tmp)
	# trial -= 1

for ele in ans:
	print ele

"""
输入数据首先包含一个整数n(1<=n<=100)，表示测试实例的个数，
然后是n行数据，每行包含一个整数m，（1<=m<=40), 表示楼梯的级数。
"""
ncase=int(raw_input().strip())
cache=[0 for i in range(41)]
cache[2],cache[3]=1,2
for i in range(4,41):
  cache[i]=cache[i-1]+cache[i-2]
for i in range(ncase):
  m=int(raw_input().strip())
  print cache[m]