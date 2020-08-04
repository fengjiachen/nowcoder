
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        ans = []
        q = []
        current_num = 0
        current_layer = []
        next_num = 0
        if pRoot != None:
            q.append(pRoot)
            current_num += 1

        while len(q) > 0 and current_num > 0:
            ele = q[0]
            current_layer.append(ele.val)
            if ele.left != None:
                q.append(ele.left)
                next_num += 1
            if ele.right != None:
                q.append(ele.right)
                next_num += 1
            q.pop(0)
            current_num -= 1
            if current_num == 0:
                ans.append(current_layer)
                current_layer = []
                if next_num != 0:
                    current_num = next_num
                    next_num = 0
        return ans


if __name__ == "__main__":
    t = TreeNode(8)
    t.left = TreeNode(6)
    t.right = TreeNode(10)
    t.left.left = TreeNode(5)
    t.left.right = TreeNode(7)
    t.right.left = TreeNode(9)
    t.right.right = TreeNode(11)
    s = Solution()
    print(s.Print(t))
