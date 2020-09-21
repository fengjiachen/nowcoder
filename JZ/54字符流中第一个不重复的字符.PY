# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.alpha = {}
        self.order = []

    def FirstAppearingOnce(self):
        # write code here
        for c in self.order:
            if self.alpha[c] == 1:
                return c
        return '#'

    def Insert(self, char):
        # write code here
        if char not in self.alpha:
            self.alpha[char] = 1
            self.order.append(char)
        else:
            self.alpha[char] += 1
