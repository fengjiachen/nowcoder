class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 == None or pRoot2 == None:
            return False
        return self.sameSubtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def sameSubtree(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val == pRoot2.val:
            return self.sameSubtree(pRoot1.left, pRoot2.left) and self.sameSubtree(pRoot1.right, pRoot2.right)
        else:
            return False
