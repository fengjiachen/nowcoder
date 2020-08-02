class Solution:
    def cutRope(self, number):
        dp = [i for i in range(number+1)]
        for i in range(number + 1):
            for cut in range(1, i):
                dp[i] = max(dp[i], dp[i - cut] * dp[cut])
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.cutRope(8))
