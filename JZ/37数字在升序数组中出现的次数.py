# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if data == None or len(data) == 0:
            return 0
        l = self.searchFirst(data, k)
        r = self.searchLast(data, k)
        if l == -1 or r == -1:
            return 0
        else:
            return r-l+1

    def searchFirst(self, data, k):
        l = 0
        r = len(data) - 1
        while l <= r:
            m = (l + r) // 2
            if data[m] > k:
                r = m - 1
            elif data[m] < k:
                l = m + 1
            else:
                if m == l or data[m - 1] != k:
                    return m
                else:
                    r = m - 1
        return - 1

    def searchLast(self, data, k):
        l = 0
        r = len(data) - 1
        while l <= r:
            m = (l + r) // 2
            if data[m] > k:
                r = m - 1
            elif data[m] < k:
                l = m + 1
            else:
                if m == r or data[m + 1] != k:
                    return m
                else:
                    l = m + 1
        return - 1
