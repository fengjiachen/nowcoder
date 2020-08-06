class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        l = 0
        r = len(rotateArray)
        if r == 0:
            return 0
        r = r-1
        while l < r:
            print(l, r)
            m = (l + r) // 2
            if rotateArray[l] >= rotateArray[r] and rotateArray[m] >= rotateArray[l]:
                l = m + 1
            else:
                r = m
        return rotateArray[l]


if __name__ == "__main__":
    l = [4, 5, 1, 2, 3]
    s = Solution()
    print(s.minNumberInRotateArray(l))
