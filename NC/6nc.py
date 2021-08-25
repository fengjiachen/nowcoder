class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        # write code here
        self.ans = 0
        if root != None:
            self.ans = root.val
            self.linkOrNot(root)
        return self.ans

    def linkOrNot(self, root):
        if root.left and root.right:
            linkLeft = self.linkOrNot(root.left)
            linkRight = self.linkOrNot(root.right)
            linkMax = max(max(linkLeft, linkRight) + root.val, root.val)
            self.ans = max(linkMax, linkLeft, linkRight,
                           linkLeft + linkRight + root.val, self.ans)
            return linkMax
        elif root.left:
            linkLeft = self.linkOrNot(root.left)
            linkMax = max(linkLeft + root.val, root.val)
            self.ans = max(linkMax, linkLeft, self.ans)
            return linkMax
        elif root.right:
            linkRight = self.linkOrNot(root.right)
            linkMax = max(linkRight + root.val, root.val)
            self.ans = max(linkMax, linkRight, self.ans)
            return linkMax
        else:
            self.ans = max(self.ans, root.val)
            return root.val
