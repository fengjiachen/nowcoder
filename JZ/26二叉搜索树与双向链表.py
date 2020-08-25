class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return pRootOfTree
        temp = pRootOfTree

        left = self.Convert(pRootOfTree.left)
        right = self.Convert(pRootOfTree.right)

        temp.right = right
        if right:
            right.left = temp
        new_head = pRootOfTree
        if left:
            new_head = left
            while left.right:
                left = left.right
            left.right = temp
            temp.left = left
        return new_head
