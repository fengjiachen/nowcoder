# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        depth = self.depth(pRoot)
        if depth == -1:
            return False
        else:
            return True

    def depth(self, pRoot):
        if pRoot == None:
            return 0
        l = self.depth(pRoot.left)
        r = self.depth(pRoot.right)
        if l == -1 or r == -1 or abs(l - r) > 1:
            return - 1
        else:
            return max(l, r)+1
