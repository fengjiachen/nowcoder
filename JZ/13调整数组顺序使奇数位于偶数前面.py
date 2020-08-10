class Solution:
    def reOrderArray(self, array):
        # write code here
        i = 0
        num_odd = 0
        for i in range(len(array)):
            if array[i] % 2 == 1:
                j = i
                while j > num_odd:
                    temp = array[j]
                    array[j] = array[j - 1]
                    array[j - 1] = temp
                    j -= 1
                num_odd += 1
        return array


if __name__ == "__main__":
    s = Solution()
    a = [1, 2, 3, 4, 5, 6]
    print(s.reOrderArray(a))
