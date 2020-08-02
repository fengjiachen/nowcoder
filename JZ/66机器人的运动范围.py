class Solution:
    def movingCount(self, threshold, rows, cols):
        if rows < 1 or cols < 1:
            return 0
        m = [[0 for _ in range(cols)] for _ in range(rows)]
        self.moving(m, 0, 0, threshold)
        return sum([sum(t) for t in m])

    def moving(self, m, i, j, threshold):
        rows = len(m)
        cols = len(m[0])
        temp = self.countNumber(i) + self.countNumber(j)
        if 0 <= i and i < rows and 0 <= j and j < cols and m[i][j] == 0 and temp <= threshold:
            m[i][j] = 1
            self.moving(m, i + 1, j, threshold)
            self.moving(m, i, j + 1, threshold)
            self.moving(m, i - 1, j, threshold)
            self.moving(m, i, j - 1, threshold)

    def countNumber(self, i):
        s = 0
        while (i > 0):
            s += i % 10
            i //= 10
        return s


if __name__ == "__main__":
    s = Solution()
    print(s.movingCount(5, 10, 10))
