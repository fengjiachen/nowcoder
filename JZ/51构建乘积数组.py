# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        l = len(A)
        left = [1 for _ in range(l)]
        right = [1 for _ in range(l)]
        for i in range(1, l ):
            left[i] = left[i - 1] * A[i-1]
        for i in range(l - 2, -1, -1):
            right[i] = right[i + 1] * A[i+1]
        B = [left[i] * right[i] for i in range(l)]
        return B


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5]
    s = Solution()
    print(s.multiply(l))
