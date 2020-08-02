class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if len(path) == 0:
            return True
        self.r = rows
        self.c = cols
        self.matrix = matrix
        for i in range(rows):
            for j in range(cols):
                if matrix[i * self.c + j] == path[0]:
                    visit = [0]*rows*cols
                    temp = self.find(visit, i, j, path)
                    if temp:
                        return True
        return False

    def find(self, visit, i, j, path):
        if len(path) == 0:
            return True
        if 0 <= i and i < self.r and 0 <= j and j < self.c and visit[i*self.c+j] == 0:
            if self.matrix[i*self.c+j] == path[0]:
                visit[i*self.c+j] = 1
                return self.find(visit, i + 1, j, path[1:]) or self.find(visit, i - 1, j, path[1:]) or self.find(visit, i, j + 1, path[1:]) or self.find(visit, i, j - 1, path[1:])
        return False


if __name__ == "__main__":
    s = Solution()
    m = 'abcesfcsadee'
    print(s.hasPath(m, 3, 4, 'bcced'))
    print(s.hasPath(m, 3, 4, 'abcb'))
    print(s.hasPath(m, 3, 4, 'abcced'))
