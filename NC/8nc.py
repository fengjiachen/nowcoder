class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root, sum):
        # write code here
        self.ans = []
        if root != None:
            self.findPath(root, sum, [])
        return self.ans

    def findPath(self, root, leftvalue, path):
        if root.left:
            path.append(root.val)
            self.findPath(root.left, leftvalue - root.val, path)
            path.pop()
        if root.right:
            path.append(root.val)
            self.findPath(root.right, leftvalue - root.val, path)
            path.pop()
        if root.left == None and root.right == None:
            if root.val == leftvalue:
                path.append(root.val)
                self.ans.append(list(path))
                path.pop()


if __name__ == '__main__':
    s = Solution()
    r = TreeNode(1)
    ans = s.pathSum(r, 1)
    print(ans)
