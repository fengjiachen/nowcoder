# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        ans = []
        q = []
        i = 0
        while size > 0 and i < len(num):
            while len(q) > 0 and num[q[-1]] < num[i]:
                q.pop()
            if len(q) > 0 and i - q[0] + 1 > size:
                q.pop(0)
            q.append(i)
            if i >= size - 1:
                ans.append(num[q[0]])
            i += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxInWindows([2, 3, 4, 2, 6, 2, 5, 1], 3))
