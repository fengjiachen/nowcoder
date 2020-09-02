# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if s == None or len(s) == 0:
            return 0
        ans = 0
        label = 1
        if s[0] == '-':
            label = -1
        i = 0
        if s[0] == '+' or s[0] == '-':
            i = 1
        for c in s[i:]:
            if c >= '0' and c <= '9':
                ans *= 10
                ans += ord(c)-ord('0')
            else:
                return 0
        return label*ans
