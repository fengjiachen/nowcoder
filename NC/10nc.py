#
# @param s string字符串 第一个整数
# @param t string字符串 第二个整数
# @return string字符串
#
class Solution:
    def solve(self, s, t):
        if s == '0' or t == '0':
            return '0'
        l = len(s) + len(t)
        ans = [0] * l
        s = s[::-1]
        t = t[::-1]
        for i in range(len(s)):
            carry = 0
            for j in range(len(t)):
                temp = int(s[i]) * int(t[j]) + carry + ans[i + j]
                ans[i + j] = temp % 10
                carry = temp // 10
            if carry > 0:
                print(carry)
                ans[i + len(t)] = carry

        if ans[-1] == 0:
            ans = ans[:-1]
        ans = ans[::-1]
        return ''.join(map(str, ans))


if __name__ == '__main__':
    s, t = "9", "99999999999999999999999999999999999999999999999999999999999994"
    a = Solution()
    print(a.solve(s, t))
