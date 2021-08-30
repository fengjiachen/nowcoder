class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
#
# @param num int整型一维数组
# @return TreeNode类
#
class Solution:
    def sortedArrayToBST(self, num):
        # write code here
        if num == None:
            return None
        else:
            return self.generateBST(num)

    def generateBST(self, num):
        l = len(num)
        if l == 0:
            return None
        elif l == 1:
            return TreeNode(num[l - 1])
        else:
            mid = l // 2
            node = TreeNode(num[mid])
            node.left = self.generateBST(num[:mid])
            node.right = self.generateBST(num[mid + 1:])
            return node