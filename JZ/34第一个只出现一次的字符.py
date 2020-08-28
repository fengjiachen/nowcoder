# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        ans = -1
        for i in range(len(s)):
            if d[s[i]] == 1:
                ans = i
                break
        return ans
