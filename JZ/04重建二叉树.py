class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0 or len(tin) == 0:
            return None
        root = TreeNode(pre[0])
        i = 0
        while i < len(tin):
            if tin[i] == pre[0]:
                break
            i += 1
        if i > 0:
            root.left = self.reConstructBinaryTree(pre[1: i + 1], tin[:i])
        if i+1 < len(tin):
            root.right = self.reConstructBinaryTree(pre[i + 1:], tin[i + 1:])
        return root
