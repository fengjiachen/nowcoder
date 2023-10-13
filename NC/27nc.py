class Solution:
    def subsets(self , S):
        # write code here
        if len(S) == 0:
            return []
        ans = [[]]
        def dfs(current, l):
            if current not in ans:
                ans.append(current)
            for i in range(len(l)):
                dfs(current+[l[i]], l[i+1:])
        curr = []
        dfs(curr, S)
        return ans

if __name__ == '__main__':
    s = Solution()
    l = [1,2,3,4]
    ans = s.subsets(l)
    print(ans)
