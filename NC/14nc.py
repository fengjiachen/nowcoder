class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        ans = []
        if pRoot == None:
            return ans
        
        stack = []
        l2r = True
        stack.append(pRoot)
        while len(stack) > 0:
            temp = []
            for i in range(len(stack)):
                root = stack.pop(0)
                temp.append(root.val)
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)
            if l2r != True:
                temp = temp[::-1]
            l2r = bool(1 - l2r)
            ans.append(temp)
        return ans