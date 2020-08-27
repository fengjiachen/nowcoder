# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput == None or len(tinput) < k:
            return []
        tinput.sort()
        return tinput[:k]
