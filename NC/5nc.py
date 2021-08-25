class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
#
# @param root TreeNode类
# @return int整型
#
class Solution:
    def sumNumbers(self, root):
        # write code here
        if root == None:
            return 0
        self.ans = 0
        self.sum(root, 0)
        return self.ans

    def sum(self, root, temp):
        if root.left:
            self.sum(root.left, temp * 10 + root.val)
        if root.right:
            self.sum(root.right, temp * 10 + root.val)
        if root.left == None and root.right == None:
            self.ans += temp * 10 + root.val


def main():
    t = TreeNode(0)
    t.left = TreeNode(1)
    t.right = TreeNode(3)
    s = Solution()
    print(s.sumNumbers(t))


if __name__ == '__main__':
    main()
