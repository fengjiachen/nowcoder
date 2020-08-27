# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        m = 1
        while m <= n:
            a = n // m
            b = n % m
            count += (a + 8) // 10 * m + (a % 10 == 1) * (b + 1)
            m *= 10
        return count
