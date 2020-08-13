class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        x_min = 0
        y_min = 0
        x_max = len(matrix)-1
        if x_max < 0:
            return []
        y_max = len(matrix[0])-1
        if y_max < 0:
            return []
        ans = []
        while x_min <= x_max and y_min <= ymax:
            for j in range(y_min, y_max):
                ans.append(matrix[xmin][j])
            xmin += 1
            for i in range(x_min, x_max):
                ans.append(matrix[i][y_max])
        return ans


if __name__ == "__main__":
    s = Solution()
    m = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
        # [13, 14, 15, 16]
    ]
    print(s.printMatrix(m))
