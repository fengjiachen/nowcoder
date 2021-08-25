class Solution:
    def maxProfit(self, prices):
        # write code here
        ans = 0
        if len(prices) <= 1:
            return ans
        buy = prices[0]
        sell = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > sell:
                sell = prices[i]
                ans = max(ans, sell - buy)
            elif prices[i] < buy:
                buy = sell = prices[i]
        return ans


def main():
    s = Solution()
    l = [1, 2, 4, 1]
    print(s.maxProfit(l))


if __name__ == '__main__':
    main()
