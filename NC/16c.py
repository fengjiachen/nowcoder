class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
#
# @param root TreeNode类
# @return bool布尔型
#
class Solution:
    def isSymmetric(self, root):
        # write code here
        if root == None:
            return True
        else:
            return self.areSymmetric(root.left, root.right)

    def areSymmetric(self, left, right):
        if left and right:
            return left.val == right.val and self.areSymmetric(
                left.left, right.right) and self.areSymmetric(
                    left.right, right.left)
        elif left == None and right == None:
            return True
        else:
            return False
