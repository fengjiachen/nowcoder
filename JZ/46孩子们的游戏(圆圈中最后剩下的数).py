# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n <= 0:
            return - 1
        elif n == 1:
            return 0
        else:
            c = range(n)
            final = -1
            start = 0
            while c:
                k = (start + m - 1) % n
                final = c.pop(k)
                n -= 1
                start = k
            return final
        # else:
        #     return (self.LastRemaining_Solution(n-1, m)+m) % n


if __name__ == "__main__":
    s = Solution()
    print(s.LastRemaining_Solution(2, 2))
