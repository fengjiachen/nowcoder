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
        while x_min <= x_max and y_min <= y_max:
            if x_min <= x_max:
                for j in range(y_min, y_max+1):
                    ans.append(matrix[x_min][j])
                x_min += 1
            if y_min <= y_max:
                for i in range(x_min, x_max+1):
                    ans.append(matrix[i][y_max])
                y_max -= 1
            if x_min <= x_max:
                for j in range(y_max, y_min - 1, -1):
                    ans.append(matrix[x_max][j])
                x_max -= 1
            if y_min <= y_max:
                for i in range(x_max, x_min - 1, -1):
                    ans.append(matrix[i][y_min])
                y_min += 1
        return ans


if __name__ == "__main__":
    s = Solution()
    m = [
        [1, 2, 3],
        [5, 6, 7],
        [9, 10, 11],
        [13, 14, 15]
    ]
    print(s.printMatrix(m))
