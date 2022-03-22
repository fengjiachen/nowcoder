class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        # write code here
        self.dfs(n, 0, 0, "")
        return self.ans

    def dfs(self, n, l, r, cur):
        if l > n or l < r:
            return
        if l == r and l == n:
            self.ans.append(cur)

        self.dfs(n, l + 1, r, cur + "(")
        self.dfs(n, l, r + 1, cur + ")")
