class Solution:
    # array 二维列表
    def Find(self, target, array):
        row = len(array)
        if row == 0:
            return False
        col = len(array[0])
        if col == 0:
            return False
        i = 0
        j = col - 1
        while i >= 0 and i < row and j >= 0 and j < col:
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
