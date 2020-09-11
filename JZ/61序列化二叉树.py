# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.depth = 0

    def Serialize(self, root):
        # write code here
        if root == None:
            return '#,'
        return str(root.val)+','+self.Serialize(root.left)+self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        nodes = s.split(',')
        self.depth = 0
        return self.des(nodes)

    def des(self, nodes):
        if self.depth >= len(nodes) or nodes[self.depth] == '#':
            self.depth += 1
            return None
        node = TreeNode(int(nodes[self.depth]))
        self.depth += 1
        node.left = self.des(nodes)
        node.right = self.des(nodes)
        return node


if __name__ == "__main__":
    s = Solution()
    t = TreeNode(8)
    t.left = TreeNode(6)
    t.right = TreeNode(10)
    t.left.left = TreeNode(5)
    t.left.right = TreeNode(7)
    t.right.left = TreeNode(9)
    t.right.right = TreeNode(11)

    print(s.Serialize(t))
    n = s.Deserialize(s.Serialize(t))
    print(s.Serialize(n))
