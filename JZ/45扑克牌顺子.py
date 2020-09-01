# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if numbers == None or len(numbers) == 0:
            return False
        numbers.sort()
        i = 0
        while i < 5 and numbers[i] == 0:
            i += 1
        j = 0
        c = i
        while i < 4:
            if numbers[i] == numbers[i + 1]:
                return False
            elif numbers[i] + 1 == numbers[i + 1]:
                i += 1
            else:
                if numbers[i + 1] - numbers[i]-1 > c:
                    return False
                else:
                    c -= numbers[i + 1] - numbers[i]-1
                    i += 1
        return True


if __name__ == "__main__":
    s = Solution()
    n = [0, 3, 2, 4, 6]
    print(s.IsContinuous(n))
