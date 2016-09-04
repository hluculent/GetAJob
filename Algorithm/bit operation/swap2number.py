# -*- coding:utf-8 -*-
"""
异或运算满足下面三条规律
0^a = a;
a^a = 0;
a^b^c = a^c^b;
"""

def swap(num_1, num_2):
    num_1 ^= num_2
    num_2 ^= num_1
    num_1 ^= num_2
    return num_1, num_2