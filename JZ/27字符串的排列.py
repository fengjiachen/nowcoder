# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        res = []
        if len(ss) < 2:
            return ss.split()
        for i in range(len(ss)):
            for n in map(lambda x: x + ss[i], self.Permutation(ss[:i] + ss[i + 1:])):
                if n not in res:
                    res.append(n)
        return sorted(res)
