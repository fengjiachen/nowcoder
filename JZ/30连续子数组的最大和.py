# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) == 0:
            return 0
        dp = [0 for _ in range(len(array))]
        ans = array[0]
        dp[0] = array[0]
        for i in range(1, len(array)):
            dp[i] = max(dp[i - 1] + array[i], array[i])
            ans = max(dp[i], ans)
        return ans
