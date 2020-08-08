class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            p = 0
            l = 1
            for i in range(2, n + 1):
                temp = p + l
                p = l
                l = temp
            return l
