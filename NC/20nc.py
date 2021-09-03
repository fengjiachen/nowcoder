# @param s string字符串
# @return string字符串一维数组
#
class Solution:
    def restoreIpAddresses(self, s):
        if len(s) < 4 or len(s) > 12:
            return []
        self.ans = []
        self.dfs(s, [])
        return self.ans

    def dfs(self, s, ips):
        if len(s) == 0:
            if len(ips) == 4:
                self.ans.append('.'.join(ips))
            return
        for i in range(1, min(4, 1 + len(s))):
            if i > 1 and s[0] == '0':
                return
            temp = int(s[:i])
            if temp > 255:
                return
            ips.append(s[:i])
            self.dfs(s[i:], ips)
            ips.pop()


if __name__ == '__main__':
    s = Solution()
    st = "25525522135"
    print(s.restoreIpAddresses(st))
    # print([i for i in range(1, 4)])
