class Solution:
    def maxsumofSubarray(self, arr):
        ans = 0
        add = 0
        for a in arr:
            add += a
            if add <= 0:
                add = 0
            else:
                ans = max(add, ans)
        return ans
