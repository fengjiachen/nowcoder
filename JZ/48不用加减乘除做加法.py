# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        while num2 != 0:
            left = (num1 ^ num2) & 0xFFFFFFFF
            num2 = ((num1 & num2) << 1) & 0xFFFFFFFF
            num1 = left
        if num1 <= 0x7fffffff:
            return num1
        else:
            return ~(num1 ^ 0xffffffff)
