class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        s = []
        result = []
        if root != None:
            s.append(root)
        while len(s) > 0:
            temp = s[0]
            s.pop(0)
            result.append(temp.val)
            if temp.left:
                s.append(temp.left)
            if temp.right:
                s.append(temp.right)
        return result
