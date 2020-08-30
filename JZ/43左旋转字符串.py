# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if len(s) == 0:
            return s
        n %= len(s)
        temp = list(s)
        while n > 0:
            c = temp[0]
            temp.pop(0)
            temp.append(c)
            n -= 1
        return ''.join(temp)
