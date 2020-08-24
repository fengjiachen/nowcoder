# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        ans = []
        if root != None:
            self.dfs(root, expectNumber, [], ans)
        return ans

    def dfs(self, root, expectNumber, current, ans):
        if expectNumber == root.val and root.left == None and root.right == None:
            ans.append(current+[root.val])
        if root.left:
            self.dfs(root.left, expectNumber-root.val, current+[root.val], ans)
        if root.right:
            self.dfs(root.right, expectNumber -
                     root.val, current+[root.val], ans)
