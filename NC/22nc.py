class Solution:
    def merge(self, A, m, B, n):
        while m - 1 >= 0 and n - 1 >= 0:
            if A[m - 1] > B[n - 1]:
                A[m + n - 1] = A[m - 1]
                m -= 1
            else:
                A[m + n - 1] = B[n - 1]
                n -= 1
        while n - 1 >= 0:
            A[n - 1] = B[n - 1]
            n -= 1
        return A


if __name__ == '__main__':
    s = Solution()
    a, b = [4, 5, 6, 0, 0, 0], [1, 2, 3]
    print(s.merge(a, 3, b, 3))
