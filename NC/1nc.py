class Solution:
    def solve(self, s, t):
        # write code here
        if len(s) < len(t):
            s, t = t, s
        lc = len(s) - len(t)
        t = '0' * lc + t
        num = [0] * (len(s) + 1)
        s = s[::-1]
        t = t[::-1]
        for i in range(0, len(s)):
            temp = int(s[i]) + int(t[i]) + num[i]
            num[i] = temp % 10
            num[i + 1] = temp // 10
        if num[-1] == 0:

            return ''.join(map(str, num[-2::-1]))
        else:
            return ''.join(map(str, num[::-1]))


def main():
    s = Solution()
    print(s.solve('1', '9'))


if __name__ == '__main__':
    main()
