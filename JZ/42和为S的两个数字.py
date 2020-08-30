# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        ans = []
        i = 0
        while i < len(array) and array[i] < (tsum - array[i]):
            j = i + 1
            for j in range(i + 1, len(array)):
                if array[i] + array[j] == tsum:
                    if len(ans) == 0:
                        ans.append(array[i])
                        ans.append(array[j])
                    else:
                        if ans[0] * ans[1] > array[i] * array[j]:
                            ans[0] = array[i]
                            ans[1] = array[j]
                elif array[i] + array[j] > tsum:
                    break
            i += 1
        return ans
