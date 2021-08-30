class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, vin):
        # write code here
        l = len(pre)
        if l == 0:
            return None
        elif l == 1:
            return TreeNode(pre[0])
        else:
            target = vin.index(pre[0])
            node = TreeNode(pre[0])
            node.left = self.reConstructBinaryTree(pre[1:1 + target],
                                                   vin[0:target])
            node.right = self.reConstructBinaryTree(pre[1 + target:],
                                                    vin[target + 1:])
            return node