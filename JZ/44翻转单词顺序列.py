# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        temp = s.split(' ')
        temp.reverse()
        return ' '.join(temp)
