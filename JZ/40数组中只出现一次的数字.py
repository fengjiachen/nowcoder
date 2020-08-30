# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if len(array) < 2:
            return 0
        elif len(array) == 2:
            return array
        temp = 0
        for a in array:
            temp ^= a
        last_one = 0
        while (temp >> last_one) & 1 == 0:
            last_one += 1
        ans = [0, 0]
        for a in array:
            if (a >> last_one) & 1 == 0:
                ans[0] ^= a
            else:
                ans[1] ^= a
        return ans
