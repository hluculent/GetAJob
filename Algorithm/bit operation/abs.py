# -*- coding:utf-8 -*-
"""
不用判断语句来实现求绝对值
"""

def bit_abs(num):
    negative = num >> 31
    return (num ^ negative) - negative