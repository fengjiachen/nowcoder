# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) == 0 and len(popV) == 0:
            return True
        stack = []
        push_i = 0
        pop_i = 0
        while push_i < len(pushV):
            if pushV[push_i] == popV[pop_i]:
                pop_i += 1
            else:
                stack.append(pushV[push_i])
            push_i += 1
        while len(stack) > 0 and pop_i < len(popV):
            if stack[-1] == popV[pop_i]:
                pop_i += 1
                stack.pop()
            else:
                return False
        if len(stack) == 0 and pop_i == len(popV):
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    print(s.IsPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(s.IsPopOrder([1, 2, 3, 4, 5], [3, 5, 4, 2, 1]))
