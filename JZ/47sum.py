# -*- coding:utf-8 -*-
class Solution:
    def Sum_Solution(self, n):
        # write code here
        s = n
        t = s and self.Sum_Solution(n - 1)
        s = s + t
        return s
