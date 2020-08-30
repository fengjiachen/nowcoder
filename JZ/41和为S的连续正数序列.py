# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        ans = []
        for i in range(1, tsum // 2 + 2):
            temp = [i]
            s = i
            for j in range(i+1, tsum // 2 + 2):
                temp.append(j)
                s += j
                if s == tsum:
                    ans.append(temp)
                    break
                elif s > tsum:
                    break
        return ans
