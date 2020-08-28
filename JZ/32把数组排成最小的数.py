# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if len(numbers) == 0:
            return ''
        num = list(map(str, numbers))
        num.sort(cmp=lambda x, y: cmp(x + y, y + x))
        ans = ''.join(num)
        return int(ans)
