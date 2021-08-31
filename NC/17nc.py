class Solution:
    def getLongestPalindrome(self, A, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        dp = [[0 for _ in range(n)] for _ in range(n)]
        ans = 1
        for i in range(n):
            dp[i][i] = 1
        for s in range(0, n - 1):
            if A[s] == A[s + 1]:
                dp[s][s + 1] = 2
                ans = max(ans, 2)
        for l in range(2, n):
            for s in range(0, n - l):
                if A[s] == A[s + l] and dp[s + 1][s + l - 1] > 0:
                    dp[s][s + l] = dp[s + 1][s + l - 1] + 2
                    ans = max(ans, dp[s][s + l])
        return ans


if __name__ == '__main__':
    s = Solution()
    a, n = "abc1234321ab", 12
    print(s.getLongestPalindrome(a, n))
