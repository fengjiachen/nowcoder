# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        count = 0
        temp_num = ''
        for n in numbers:
            if temp_num == n:
                count += 1
            else:
                if count == 0:
                    temp_num = n
                    count += 1
                else:
                    count -= 1
        count = 0
        for n in numbers:
            if n == temp_num:
                count += 1
        if count > len(numbers) / 2.0:
            return temp_num
        else:
            return 0


if __name__ == "__main__":
    num = [4, 2, 4, 1, 4, 2]
    s = Solution()
    print(s.MoreThanHalfNum_Solution(num))
