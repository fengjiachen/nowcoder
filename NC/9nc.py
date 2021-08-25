class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
#
# @param root TreeNode类
# @param sum int整型
# @return bool布尔型
#
class Solution:
    def hasPathSum(self, root, sum):
        # write code here
        if root == None:
            return False
        return self.pathSum(root, sum)

    def pathSum(self, root, leftValue):
        left = False
        right = False
        if root.left:
            left = self.pathSum(root.left, leftValue - root.val)
            if left == True:
                return True
        if root.right:
            right = self.pathSum(root.right, leftValue - root.val)
            if right == True:
                return right
        if root.left == None and root.right == None:
            return root.val == leftValue


if __name__ == '__main__':
    s = Solution()
    r = TreeNode(1)
    r.left = TreeNode(2)
    print(s.hasPathSum(r, 3))
