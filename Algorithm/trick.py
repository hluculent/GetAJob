# -*- coding:utf-8 -*-
"""
写一个程序，打印数字1到100，
3的倍数打印“Fizz”来替换这个数，5的倍数打印“Buzz”，
对于既是3的倍数又是5的倍数的数字打印“FizzBuzz”。
"""
for x in range(101):
    print "fizz"[x % 3 * 4::]+"buzz"[x % 5 * 4::] or x
# 只有是3或者5的倍数的时候，=0 才正确切片，
# 其它数值时，由于 *4 所以过界，所以不会出现字符串
# print 'aaa'[2::] >>> a
