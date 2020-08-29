# -*- coding:utf-8 -*-
from collections import deque


class Solution:
    def __init__(self):
        self.count = 0

    def InversePairs(self, data):
        # write code here
        self.mergeSort(data)
        return self.count % 1000000007

    def mergeSort(self, l):
        if len(l) < 2:
            return l
        mid = len(l) // 2
        left = self.mergeSort(l[:mid])
        right = self.mergeSort(l[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        merged = []
        while len(left) > 0 and len(right) > 0:
            if left[0] > right[0]:
                self.count += len(left)
                self.count %= 1000000007
                merged.append(right[0])
                right.pop(0)
            else:
                merged.append(left[0])
                left.pop(0)
        if len(left) > 0:
            merged.extend(left)
        if len(right) > 0:
            merged.extend(right)
        return merged

# 以上代码超时 主要是list直接使用导致的
# 使用deque双向队列能够避免超时，以下为参考代码

# class Solution:
#     def __init__(self):
#         self.count = 0

#     def InversePairs(self, lis):
#         # write code here
#         self.mergeSort(lis)
#         return self.count % 1000000007

#     def mergeSort(self, lis):
#         if len(lis) <= 1:
#             return lis
#         middle = int(len(lis)//2)
#         left = self.mergeSort(lis[:middle])
#         right = self.mergeSort(lis[middle:])
#         return self.merge(left, right)

#     def merge(self, left, right):
#         merged, left, right = deque(), deque(left), deque(right)
#         while left and right:
#             if left[0] > right[0]:
#                 self.count += len(left)
#                 merged.append(right.popleft())
#             else:
#                 merged.append(left.popleft())
#         if right:
#             merged.extend(right)
#         else:
#             merged.extend(left)
#         return merged


if __name__ == "__main__":
    s = Solution()
    l = [1, 2, 3, 4, 5, 6, 7, 1, 0]
    print(s.InversePairs(l))
