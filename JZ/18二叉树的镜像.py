class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root == None:
            return root
        temp = root.left
        root.left = self.Mirror(root.right)
        root.right = self.Mirror(temp)
        return root
