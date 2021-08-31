class Solution:
    def rotateMatrix(self, mat, n):
        # write code here
        if n <= 1:
            return mat
        for c in range(n // 2 + 1):
            if c >= (n - c - 1):
                break
            for i in range(0, n - 2 * c - 1):
                temp = mat[c][c + i]
                mat[c][c + i] = mat[n - c - i - 1][c]
                mat[n - c - i - 1][c] = mat[n - c - 1][n - c - i - 1]
                mat[n - c - 1][n - c - i - 1] = mat[c + i][n - c - 1]
                mat[c + i][n - c - 1] = temp
        return mat


if __name__ == '__main__':
    s = Solution()
    mat, n = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3
    print(s.rotateMatrix(mat, n))
