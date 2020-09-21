# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isIntOrFloat(self, s):
        i = 0
        point = False
        if s[0] == '+' or s[0] == '-':
            i += 1
        for c in s[i:]:
            if c == '.' and point == False:
                point = True
            elif c >= '0' and c <= '9':
                continue
            else:
                return False
        return True

    def isInt(self, s):
        i = 0
        if s[0] == '+' or s[0] == '-':
            i += 1
        for c in s[i:]:
            if c >= '0' and c <= '9':
                continue
            else:
                return False
        return True

    def isNumeric(self, s):
        # write code here
        if 'e' in s:
            part = s.split('e')
            if len(part[1]) == 0:
                return False
            return self.isIntOrFloat(part[0]) and self.isInt(part[1])
        elif 'E' in s:
            part = s.split('E')
            if len(part[1]) == 0:
                return False
            return self.isIntOrFloat(part[0]) and self.isInt(part[1])
        else:
            return self.isIntOrFloat(s)


if __name__ == "__main__":
    s = Solution()
    print(s.isNumeric('12e'))
