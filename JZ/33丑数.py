# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        ans = [0, 1]
        p2 = 1
        p3 = 1
        p5 = 1
        for i in range(1, index+1):
            temp_ugly = min(ans[p2] * 2, ans[p3] * 3, ans[p5] * 5)
            if temp_ugly == ans[p2] * 2:
                p2 += 1
            if temp_ugly == ans[p3] * 3:
                p3 += 1
            if temp_ugly == ans[p5] * 5:
                p5 += 1
            ans.append(temp_ugly)
        return ans[index]
